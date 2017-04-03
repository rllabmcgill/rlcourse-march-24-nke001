import os
import sys
from model import train


def main(path=None):
    
    train(num_epochs = 200,
        step_epoch = 5000,
        step_test = 0,
        path = path,
        frame_skip = 4,
        repeat_action_probability = 0,
        update_rule = 'deepmind_rmsprop',
        batch_accumulator = 'sum',
        lr = 0.00025,
        discount = 0.95,
        rms_decay = 0.95,
        rms_eps = 0.01,
        momentum = 0,
        clip_delta = 1.0,
        eps_start = 1.0,
        eps_min = 0.005,
        eps_length = 4,
        phi_length = 4,
        update_frequency = 4,
        replay_mem_size = 10000000,
        batch_size = 32,
        network_type = 'nature_mlp',
        replay_start_size=50000,
        resize_method = 'scale',
        resized_width = 84,
        resized_height = 84,
        death_ends_episode = 'true',
        max_start_nullops = 30,
        deterministic = True,
        cudnn_deterministic = False,
        episodic_control = True,
        k_neighbor = 11,
        ec_discount = 1.0,
        buffer_size = 1.0,
        dim_state = 64,
        projection_type = 'random')

if name=='__main__':
    main(path='output')




