"""
    Testing broken object property level authorization (BOLA) vulnerabilities
"""
    
import pytest
import allure
from allure_commons.types import Severity
from your_module import Object, ObjectManager, User

# TODO - CONFIGURE THIS POC FOR DEMOQA


@pytest.fixture
def sample_objects():
    obj1 = Object("document.txt", "alice")
    obj2 = Object("image.jpg", "bob")
    return [obj1, obj2]


@pytest.fixture
def object_manager(sample_objects):
    manager = ObjectManager()
    for obj in sample_objects:
        manager.add_object(obj)
    return manager


@pytest.fixture
def admin_user():
    return User("admin", "admin")


@pytest.fixture
def alice_user():
    return User("alice", "user")


@pytest.fixture
def bob_user():
    return User("bob", "user")


@pytest.mark.security
@allure.title("Test For Broken Object Property Level Authorization (BOLA)")
@allure.description("API3:2023 Broken Object Property Level Authorization")
@allure.severity(Severity.CRITICAL)
def test_admin_can_delete_any_object(object_manager, admin_user):
    with allure.step("Confirm administrator can perform delete action on object manager"):
        assert object_manager.delete_object(admin_user, "document.txt") == "Object 'document.txt' deleted successfully."


def test_owner_can_delete_own_object(object_manager, alice_user):
    with allure.step("Confirm super-user can perform delete action on object manager"):
        assert object_manager.delete_object(alice_user, "document.txt") == "Object 'document.txt' deleted successfully."


def test_non_owner_cannot_delete_object(object_manager, bob_user):
    with allure.step("Confirm user cannot perform delete action on object manager"):
        assert object_manager.delete_object(bob_user, "document.txt") == "You are not authorized to delete this object."


def test_nonexistent_object(object_manager, alice_user):
    with allure.step("Confirm error shown for non-existent object manager"):
        assert object_manager.delete_object(alice_user, "nonexistent.txt") == "Object 'nonexistent.txt' not found."
