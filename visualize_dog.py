import time
import mujoco as mj
from mujoco import viewer
import numpy as np


def view_dog():
    """
    Load dog.xml and make it move with sinusoidal controls.
    """
    model = mj.MjModel.from_xml_path("floor_dog.xml")
    data = mj.MjData(model)

    dt = model.opt.timestep
    t = 0.0
    viewer2 = viewer.launch_passive(model, data)

    # 每条腿 3 个关节，一共 12 个
    n = model.nu
    phases = np.linspace(0, np.pi, n, endpoint=False)  # 给每个关节分个相位差

    while True:
        mj.mj_step(model, data)

        # 控制量：正弦波 + 相位差
        data.ctrl[:] = 0.5 * np.sin(2 * np.pi * 1.0 * t + phases)

        t += dt
        time.sleep(dt)
        viewer2.sync()


if __name__ == "__main__":
    view_dog()
