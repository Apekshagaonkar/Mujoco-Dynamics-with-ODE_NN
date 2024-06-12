from mujoco_physics import HopperPhysics
import torch
import os
from lib.plotting import plot_trajectories
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# #generating the trajectories and loading the .pt file
# dataset_obj = HopperPhysics(root='data', download=False, generate=True, device = device)

# root = r"C:\Users\msi\Desktop\ECE-228\Project\latent_ode\data\HopperPhysics\training.pt"

# dataset =torch.load(root)

# print(type(dataset))
# print(dataset.shape)
# print("First sample, first time step:", dataset[0, 0, :])

# output_dir = 'hopper_imgs'
# os.makedirs(output_dir, exist_ok=True)

#to get the frames saved for vizualization inside hopper_imgs
hopper = HopperPhysics(root='data', download=False, generate=False)

dataset = hopper.get_dataset()
print(dataset.shape)
traj_index = 23   # Index of the trajectory you want to visualize
trajectory = dataset[traj_index]
print(trajectory.shape)
n_timesteps =trajectory.shape[0]
time_steps = torch.linspace(0, 10, n_timesteps).to(trajectory.device) 
n_dims = trajectory.shape[1]
fig, axes = plt.subplots(nrows=7, ncols=2, figsize=(15, 20))  # Create a grid of subplots
axes = axes.flatten()
# hopper.visualize(trajectory, plot_name=f'traj_{traj_index}', dirname=output_dir)
for i in range(n_dims):
    ax = axes[i]
    plot_trajectories(ax, trajectory.unsqueeze(0), time_steps, title=f"Dimension {i}", dim_to_show=i, add_legend=True)


plt.tight_layout()
plt.show()


# # the visual environment I showed first during the meeting, with the mouse.
# from dm_control import suite
# from dm_control import viewer
# import numpy as np

# env = suite.load(domain_name="humanoid", task_name="run")
# action_spec = env.action_spec()

# # Define a uniform random policy.
# def random_policy(time_step):
#   del time_step  # Unused.
#   return np.random.uniform(low=action_spec.minimum,
#                            high=action_spec.maximum,
#                            size=action_spec.shape)

# # Launch the viewer application.
# viewer.launch(env, policy=random_policy)