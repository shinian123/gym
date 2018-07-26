from gym import utils
from gym.envs.robotics import bulldog_env


class BulldogPickAndPlaceEnv(bulldog_env.BulldogEnv, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_qpos = {
            'front_left_wheel_joint':0,
            'front_right_wheel_joint':0,
            'rear_left_wheel_joint':0,
            'rear_right_wheel_joint':0,
            'left_arm_shoulder_pan_joint':0,
            'left_arm_shoulder_lift_joint':0,
            'left_arm_elbow_joint':0,
            'left_arm_wrist_1_joint':0,
            'left_arm_wrist_2_joint':0,
            'left_arm_wrist_3_joint':0,
            'left_gripper_palm_finger_1_joint':0,
            'left_gripper_finger_1_joint_1':0,
            'left_gripper_finger_1_joint_2':0,
            'left_gripper_finger_1_joint_3':0,
            'left_gripper_palm_finger_2_joint':0,
            'left_gripper_finger_2_joint_1':0,
            'left_gripper_finger_2_joint_2':0,
            'left_gripper_finger_2_joint_3':0,
            'left_gripper_finger_middle_joint_1':0,
            'left_gripper_finger_middle_joint_2':0,
            'left_gripper_finger_middle_joint_3':0,
            'right_arm_shoulder_pan_joint':0,
            'right_arm_shoulder_lift_joint':0,
            'right_arm_elbow_joint':0,
            'right_arm_wrist_1_joint':0,
            'right_arm_wrist_2_joint':0,
            'right_arm_wrist_3_joint':0,
            'right_gripper_palm_finger_1_joint':0,
            'right_gripper_finger_1_joint_1':0,
            'right_gripper_finger_1_joint_2':0,
            'right_gripper_finger_1_joint_3':0,
            'right_gripper_palm_finger_2_joint':0,
            'right_gripper_finger_2_joint_1':0,
            'right_gripper_finger_2_joint_2':0,
            'right_gripper_finger_2_joint_3':0,
            'right_gripper_finger_middle_joint_1':0,
            'right_gripper_finger_middle_joint_2':0,
            'right_gripper_finger_middle_joint_3':0,
        }
        bulldog_env.BulldogEnv.__init__(
            self, 'bulldog/pick_and_place.xml', has_object=True, block_gripper=False, n_substeps=20,
            gripper_extra_height=0.2, target_in_the_air=True, target_offset=0.0,
            obj_range=0.15, target_range=0.15, distance_threshold=0.05,
            initial_qpos=initial_qpos, reward_type=reward_type)
        utils.EzPickle.__init__(self)
