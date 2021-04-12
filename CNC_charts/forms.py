from django import forms
import CNC_charts.models as m
from django import forms
import CNC_charts.models as m

class OperatorForm(forms.ModelForm):
      class Meta:
          model = m.Operator_Data
          fields = '__all__'

class EngineerForm(forms.ModelForm):
      class Meta:
          model = m.Engineer_Data
          fields = '__all__'

class TypeForm(forms.ModelForm):
    class Meta:
        model = m.Type_Table
        fields = "__all__"

class ShiftForm(forms.ModelForm):
    class Meta:
        model = m.Shift_table
        fields = '__all__'

class PlanDowntimeForm(forms.ModelForm):
    class Meta:
        model = m.plan_downtime_table
        fields = '__all__'
        # shift = forms.ModelMultipleChoiceField(queryset=(m.Shift_table.objects.filter("shift")))
        # Cnc = forms.ModelMultipleChoiceField(queryset=m.CNC_ID.objects.all().filter("Cnc.name"))
        # Operator = forms.ModelMultipleChoiceField(queryset=m.Operator_Data.objects.filter("name"))

class UnplanDowntimeForm(forms.ModelForm):
    class Meta:
        model = m.Unplan_downtime_table
        fields = '__all__'
        # shift = forms.ModelMultipleChoiceField(queryset=(m.Shift_table.objects.filter("shift")))
        # Cnc = forms.ModelMultipleChoiceField(queryset=m.CNC_ID.objects.filter("Cnc_name"))
        # Operator = forms.ModelMultipleChoiceField(queryset=m.Operator_Data.objects.filter("name"))
