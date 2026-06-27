import time
import uuid
from playwright.sync_api import Playwright

BASE = "https://petstore.swagger.io/v2"

def make_pet_payload(cat_name: str, pet_id: int = None) -> dict:
	if pet_id is None:
		pet_id = int(time.time() * 1000) % 100000000
	return {
		"id": pet_id,
		"category": {"id": 0, "name": cat_name},
		"name": "Doggie",
		"photoUrls": ["string"],
		"tags": [{"id": 0, "name": "string"}],
		"status": "available",
	}

def test_create_pet_post_basic(playwright: Playwright):
	"""POST a new pet and verify response code and JSON values using Playwright request."""
	api = playwright.request.new_context(base_url=BASE)
	payload = make_pet_payload("cat-basic")
	r = api.post("/pet", json=payload)
	assert r.status == 200
	data = r.json()
	assert data["id"] == payload["id"]
	assert data["name"] == payload["name"]
	assert data["category"]["name"] == "cat-basic"
	api.dispose()

def test_create_pet_post_with_cleanup(playwright: Playwright):
	"""POST a pet with a unique category name, verify fields, then delete it using Playwright request."""
	api = playwright.request.new_context(base_url=BASE)
	unique_cat = f"cat-{uuid.uuid4().hex[:8]}"
	pet_id = int(time.time() * 1000) % 100000000
	payload = make_pet_payload(unique_cat, pet_id=pet_id)

	resp = api.post("/pet", json=payload)
	assert resp.status == 200
	body = resp.json()
	assert body.get("id") == payload["id"]
	assert body.get("name") == "Doggie"
	assert body.get("category", {}).get("name") == unique_cat

	# cleanup - delete the created pet
	dr = api.delete(f"/pet/{pet_id}")
	# API may return 200 for successful delete
	assert dr.status in (200, 202, 204)
	api.dispose()


def test_get_pets_by_status(playwright: Playwright):
	"""GET pets by status and verify response and at least one item has requested status using Playwright request."""
	api = playwright.request.new_context(base_url=BASE)
	status = "available"
	r = api.get("/pet/findByStatus", params={"status": status})
	assert r.status == 200
	data = r.json()
	# if there's at least one returned, verify its status
	if len(data) > 0:
		assert all((p.get("status") == status or p.get("status") == status) for p in data)
	api.dispose()


def test_get_pet_by_id_and_update(playwright: Playwright):
	"""Create a pet, GET by id, update details via PUT, verify the update, then delete using Playwright request."""
	api = playwright.request.new_context(base_url=BASE)
	unique_cat = f"cat-{uuid.uuid4().hex[:8]}"
	pet_id = int(time.time() * 1000) % 100000000
	payload = make_pet_payload(unique_cat, pet_id=pet_id)

	# create
	resp = api.post("/pet", json=payload)
	assert resp.status == 200

	# get by id
	rget = api.get(f"/pet/{pet_id}")
	assert rget.status == 200
	body = rget.json()
	assert body.get("id") == pet_id
	assert body.get("category", {}).get("name") == unique_cat

	# update details: change name and status
	payload["name"] = "DoggieUpdated"
	payload["status"] = "sold"
	rput = api.put("/pet", json=payload)
	assert rput.status == 200
	updated = rput.json()
	assert updated.get("name") == "DoggieUpdated"
	assert updated.get("status") == "sold"

	# verify via get
	rget2 = api.get(f"/pet/{pet_id}")
	assert rget2.status == 200
	assert rget2.json().get("name") == "DoggieUpdated"

	# cleanup
	dr = api.delete(f"/pet/{pet_id}")
	assert dr.status in (200, 202, 204)
	api.dispose()


def test_form_update_large_id(playwright: Playwright):
	"""Create a pet with a very large ID, update via form-encoded POST and verify using Playwright request."""
	api = playwright.request.new_context(base_url=BASE)
	pet_id = 9223372036854775807
	payload = make_pet_payload("cat-large", pet_id=pet_id)

	# create the pet
	r = api.post("/pet", json=payload)
	assert r.status == 200

	# perform the form-encoded update with headers
	headers = {
		"api_key": "test",
		"Content-Type": "application/x-www-form-urlencoded",
	}
	data = {"name": "test1", "status": "pending"}
	rf = api.post(f"/pet/{pet_id}", headers=headers, data=data)
	assert rf.status in (200, 201)

	# verify updated values via GET
	rget = api.get(f"/pet/{pet_id}")
	assert rget.status == 200
	body = rget.json()
	assert body.get("name") == "test1"
	assert body.get("status") == "pending"

	# cleanup
	dr = api.delete(f"/pet/{pet_id}")
	assert dr.status in (200, 202, 204)
	api.dispose()

