from module_processing.arrk.Calculator.Calculation.Instructions.CurveCalculationInstruction import CurveCalculationInstruction
from module_misc.Curves import Curves


class CurveCalculationInstructionSubtract(CurveCalculationInstruction):
    def __init__(self, parameters):
        super().__init__(parameters, "subtraction", in_min_length_required=2, out_length_required=1)

    def calculate(self, curves: Curves, values: dict):
        curve_diff = curves.get_curve(self._curve_names[0])
        for curve_name in self._curve_names[1:]:
            curve_diff = curve_diff - curves.get_curve(curve_name)
        curves.add_curve(curve_diff, self._result_curves[0])

    def generate(self):
        self.extract()
        self.get_arguments()
