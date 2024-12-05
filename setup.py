#arquivo para criar o executavel
import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name="Layers of Discrete Mathematics",
    options = {"build_exe":{"packages":["pygame", "math"],
                            'include_files':['assets']}},
    executables = executables
)
