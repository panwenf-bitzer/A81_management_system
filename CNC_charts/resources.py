from import_export import resources
from .models import Attendance_Master , Operator_Data

class AttendanceResources(resources.ModelResource):
    class Meta:
        model = Attendance_Master
class OperatorResources(resources.ModelResource):
    class Meta:
        model = Operator_Data