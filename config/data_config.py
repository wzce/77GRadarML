import os

config_type = 5


class DataConfig:
    project_base = 'D:\home\zeewei\projects\\77GRadarML\\'
    origin_train_data_dir = 'D:\\home\\zeewei\\20190319\\line1_train\\'
    origin_val_data_dir = 'D:\home\zeewei\\20190319\line1_val'
    processed_data_dir = os.path.join(project_base, 'processed_data\\train_val_data_0409')
    train_data_file_name = 'one_line_train_0409.npy'
    val_data_file_name = 'one_line_val_0409.npy'

    train_result_log = 'train_one_line_log.npy'
    cnn_model_save_dir = os.path.join(project_base, 'model\cnn\model_dir\cnn2_1')
    rnn_model_save_dir = os.path.join(project_base, 'model\\rnn\model_save_dir\\rnn2_1_one_0409_2')

    train_data_input = 'pg_train_data_input.npy'
    train_data_label = 'pg_train_data_label.npy'
    test_data_input = 'pg_test_data_input.npy'
    test_data_label = 'pg_test_data_label.npy'

    train_parameter_file = os.path.join(project_base, 'model\cnn\model_dir\\train_cnn2_1_0410_2.npy')

    def __init__(self):
        pass


class MutiGoalDataConfig(DataConfig):
    project_base = 'D:\home\zeewei\projects\\77GRadarML\\'
    origin_train_data_dir = 'D:\home\zeewei\\20190612\\train'
    origin_val_data_dir = 'D:\home\zeewei\\20190612\\val'
    processed_data_dir = os.path.join(project_base, 'processed_data\\train_val_data_0613')
    train_data_file_name = 'one_line_train_0613.npy'
    val_data_file_name = 'one_line_val_0613.npy'

    train_result_log = 'train_two_line_log.npy'
    cnn_model_save_dir = os.path.join(project_base, 'model\cnn\model_dir\cnn2_1_0613')
    rnn_model_save_dir = os.path.join(project_base, 'model\\rnn\model_save_dir\\rnn2_1_one_0613_2')

    train_parameter_file = os.path.join(project_base, 'model\cnn\model_dir\\train_cnn2_1_0613.npy')

    def __init__(self):
        pass


class MutiGoalDataConfig_OneTime(MutiGoalDataConfig):
    project_base = 'D:\home\zeewei\projects\\77GRadarML\\'
    origin_train_data_dir = 'D:\home\zeewei\\20190612\one_time\\train'
    origin_val_data_dir = 'D:\home\zeewei\\20190612\one_time\\val'
    processed_data_dir = os.path.join(project_base, 'processed_data\\train_val_data_0613_onetime')
    train_data_file_name = 'one_line_train_0613_onetime.npy'
    val_data_file_name = 'one_line_val_0613_onetime.npy'

    train_result_log = 'train_two_line_log_0613_onetime.npy'
    cnn_model_save_dir = os.path.join(project_base, 'model\cnn\model_dir\cnn2_1_0613_onetime')
    # rnn_model_save_dir = os.path.join(project_base, 'model\\rnn\model_save_dir\\rnn2_1_one_0613_2')

    train_parameter_file = os.path.join(project_base, 'model\cnn\model_dir\\train_cnn2_1_0613_onetime.npy')

    def __init__(self):
        pass


class TwoGoalsDataConfig(DataConfig):
    project_base = 'D:\home\zeewei\projects\\77GRadarML\\'
    origin_train_data_dir = 'D:\home\zeewei\ML_data\\two_goal\\train'
    origin_val_data_dir = 'D:\home\zeewei\ML_data\\two_goal\\val'
    processed_data_dir = os.path.join(project_base, 'processed_data\\two_goals')
    train_data_file_name = 'two_goal_train.npy'
    val_data_file_name = 'two_goal_val.npy'

    train_result_log = 'train_two_goal_log.npy'
    cnn_model_save_dir = os.path.join(project_base, 'model\cnn\model_dir\cnn2_1_two_goals')
    rnn_model_save_dir = os.path.join(project_base, 'model\\rnn\model_save_dir\\rnn2_1_two_goals')

    train_parameter_file = os.path.join(project_base, 'model\cnn\model_dir\\cnn2_1_two_goals.npy')

    def __init__(self):
        pass


class MixGoalsDataConfig(DataConfig):
    project_base = 'D:\home\zeewei\projects\\77GRadarML\\'
    origin_train_data_dir = 'D:\home\zeewei\ML_data\\mix_goal\\train'
    origin_val_data_dir = 'D:\home\zeewei\ML_data\\mix_goal\\val'
    processed_data_dir = os.path.join(project_base, 'processed_data\\mix_goals')
    train_data_file_name = 'mix_goal_train.npy'
    val_data_file_name = 'mix_goal_val.npy'

    train_result_log = 'train_mix_goal_log.npy'
    cnn_model_save_dir = os.path.join(project_base, 'model\cnn\model_dir\\cnn_2_1_mix_goal_limit_range')
    rnn_model_save_dir = os.path.join(project_base, 'model\\rnn\model_save_dir\\rnn2_1_mix_goals')

    train_parameter_file = os.path.join(project_base, 'model\cnn\model_dir\\cnn2_1_mix_goals.npy')

    def __init__(self):
        pass

class LinuxDataConfig(DataConfig):
    origin_train_data_dir = '/home/wzce/radar_data/data_line1/'
    process_data_dir = '/home/wzce/radar_data/processed_data/line1/'
    train_data_file_name = 'one_line_train_data_0408.npy'
    val_data_file_name = 'one_line_val_data_0408.npy'

    train_result_log = 'train_one_line_logs.npy'
    model_save_dir = '/home/wzce/radar_data/rnn/rnn2_1_0409/'

    def __init__(self):
        pass


def fetch_config():
    if config_type == 5:
        config = MixGoalsDataConfig()
    elif config_type == 4:
        config = TwoGoalsDataConfig()
    elif config_type == 3:
        config = LinuxDataConfig()
    elif config_type == 2:
        config = MutiGoalDataConfig_OneTime()
    elif config_type == 1:
        config = MutiGoalDataConfig()
    else:
        config = DataConfig()
    return config
