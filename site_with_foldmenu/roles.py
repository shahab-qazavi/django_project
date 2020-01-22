from rolepermissions.roles import AbstractUserRole


class DeleteImg(AbstractUserRole):

    available_permissions = {
        'can_delete_image': True,
    }


class AddImg(AbstractUserRole):

    available_permissions = {
     'can_add_image': True,
    }


class AddUser(AbstractUserRole):
    available_permissions = {
        'can_add_users': True,
    }


class EditUsers(AbstractUserRole):
    available_permissions = {
        'can_edit_users': True,
    }


class DeleteUsers(AbstractUserRole):
    available_permissions = {
        'can_delete_users': True,
    }


class SeeUsers(AbstractUserRole):
    available_permissions = {
        'can_see_users': True,
    }


class Doctor(AbstractUserRole):
    available_permissions = {
        'create_medical_record': True,
    }


class Nurse(AbstractUserRole):
    available_permissions = {
        'edit_patient_file': True,
    }

