import os
from Transparency.common_code.common import *

def generate_basic_config(dataset, exp_name) :
    config = {
        'model' :{
            'encoder' : {
                'vocab_size' : dataset.vec.vocab_size,
                'embed_size' : dataset.vec.word_dim
            },
            'decoder' : {
                'attention' : {
                    'type' : 'tanh'
                },
                'output_size' : dataset.output_size
            }
        },
        'training' : {
            'bsize' : dataset.bsize if hasattr(dataset, 'bsize') else 32,
            'weight_decay' : 1e-5,
            'pos_weight' : dataset.pos_weight if hasattr(dataset, 'pos_weight') else None,
            'basepath' : dataset.basepath if hasattr(dataset, 'basepath') else 'outputs',
            'exp_dirname' : os.path.join(dataset.name, exp_name)
        }
    }

    return config

def generate_lstm_config(dataset) :
    config = generate_basic_config(dataset, exp_name='lstm+tanh')
    hidden_size = dataset.hidden_size if hasattr(dataset, 'hidden_size') else 128
    config['model']['encoder'].update({'type': 'rnn', 'hidden_size' : hidden_size})
    return config

def generate_gru_config(dataset) :
    config = generate_basic_config(dataset, exp_name='gru+tanh')
    hidden_size = dataset.hidden_size if hasattr(dataset, 'hidden_size') else 128
    config['model']['encoder'].update({'type': 'gru', 'hidden_size' : hidden_size})
    return config

def generate_mono_lstm_config(dataset) :
    config = generate_basic_config(dataset, exp_name='mono-lstm+tanh')
    hidden_size = dataset.hidden_size if hasattr(dataset, 'hidden_size') else 128
    config['model']['encoder'].update({'type': 'mono-lstm', 'hidden_size' : hidden_size})
    return config

def generate_average_config(dataset) :
    config = generate_basic_config(dataset, exp_name='average+tanh')
    hidden_size = dataset.hidden_size if hasattr(dataset, 'hidden_size') else 128
    config['model']['encoder'].update({'projection' : True, 'hidden_size' : hidden_size, 'activation' : 'tanh', 'type' : 'average'})
    return config

def generate_cnn_config(dataset, filters=(1, 3, 5, 7)) :
    config = generate_basic_config(dataset, exp_name='cnn' + str(filters).replace(' ', '') + '+tanh')
    hidden_size = dataset.hidden_size if hasattr(dataset, 'hidden_size') else 128
    config['model']['encoder'].update({'kernel_sizes': filters, 'hidden_size' : hidden_size // len(filters), 'activation' : 'relu', 'type': 'cnn'})
    return config

def generate_vanilla_lstm_config(dataset) :
    config = generate_lstm_config(dataset)
    config['model']['decoder']['use_attention'] = False
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'lstm')
    return config

def generate_vanilla_gru_config(dataset) :
    config = generate_gru_config(dataset)
    config['model']['decoder']['use_attention'] = False
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'gru')
    return config

def generate_vanilla_mono_lstm_config(dataset) :
    config = generate_mono_lstm_config(dataset)
    config['model']['decoder']['use_attention'] = False
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'mono_lstm')
    return config

def generate_logodds_config(dataset) :
    config = generate_lstm_config(dataset)
    model = get_latest_model(os.path.join('outputs', dataset.name, 'LR+TFIDF'))
    config['model']['decoder']['attention'] = {
        'type' : 'logodds',
        'logodds_file' : os.path.join(model, 'logodds.p')
    }
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'lstm+logodds')
    return config

def generate_logodds_config_gru(dataset) :
    config = generate_gru_config(dataset)
    model = get_latest_model(os.path.join('outputs', dataset.name, 'LR+TFIDF'))
    config['model']['decoder']['attention'] = {
        'type' : 'logodds',
        'logodds_file' : os.path.join(model, 'logodds.p')
    }
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'gru+logodds')
    return config

def generate_logodds_config_mono(dataset) :
    config = generate_mono_lstm_config(dataset)
    model = get_latest_model(os.path.join('outputs', dataset.name, 'LR+TFIDF'))
    config['model']['decoder']['attention'] = {
        'type' : 'logodds',
        'logodds_file' : os.path.join(model, 'logodds.p')
    }
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'mono-lstm+logodds')
    return config

def generate_logodds_regularised_config(dataset) :
    config = generate_lstm_config(dataset)
    model = get_latest_model(os.path.join('outputs', dataset.name, 'LR+TFIDF'))
    config['model']['decoder']['regularizer_attention'] = {
        'type' : 'logodds',
        'logodds_file' : os.path.join(model, 'logodds.p')
    }
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'lstm+logodds(Reg)')
    return config

def generate_logodds_regularised_config_gru(dataset) :
    config = generate_gru_config(dataset)
    model = get_latest_model(os.path.join('outputs', dataset.name, 'LR+TFIDF'))
    config['model']['decoder']['regularizer_attention'] = {
        'type' : 'logodds',
        'logodds_file' : os.path.join(model, 'logodds.p')
    }
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'gru+logodds(Reg)')
    return config

def generate_logodds_regularised_config_mono(dataset) :
    config = generate_mono_lstm_config(dataset)
    model = get_latest_model(os.path.join('outputs', dataset.name, 'LR+TFIDF'))
    config['model']['decoder']['regularizer_attention'] = {
        'type' : 'logodds',
        'logodds_file' : os.path.join(model, 'logodds.p')
    }
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'mono-lstm+logodds(Reg)')
    return config

def generate_vanilla_cnn_config(dataset) :
    config = generate_cnn_config(dataset)
    config['model']['decoder']['use_attention'] = False
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'cnn')
    return config

def generate_single_cnn_config(dataset) :
    config = generate_cnn_config(dataset, filters=(3,))
    config['training']['exp_dirname'] = os.path.join(dataset.name, 'cnn(3)+tanh')
    return config

def make_attention_dot(func) :
    def new_func(dataset) :
        config = func(dataset)
        config['model']['decoder']['attention']['type'] = 'dot'
        config['training']['exp_dirname'] = config['training']['exp_dirname'].replace('tanh', 'dot')
        return config

    return new_func

configurations = {
    'vanilla_lstm' : generate_vanilla_lstm_config,
    'vanilla_cnn' : generate_vanilla_cnn_config,
    'vanulla_gru' : generate_vanilla_gru_config,
    'vanulla_mono_lstm' : generate_vanilla_mono_lstm_config,
    'lstm' : generate_lstm_config,
    'gru' : generate_gru_config,
    'mono-lstm' : generate_mono_lstm_config,
    'average' : generate_average_config,
    'cnn' : generate_cnn_config,
    'logodds_lstm' : generate_logodds_config,
    'logodds_gru' : generate_logodds_config_gru,
    'logodds_mono_lstm' : generate_logodds_config_mono,
    'logodds_lstm_reg' : generate_logodds_regularised_config,
    'logodds_gru_reg' : generate_logodds_regularised_config_gru,
    'logodds_mono_lstm_reg' : generate_logodds_regularised_config_mono,
    'single_cnn' : generate_single_cnn_config,
    'lstm_dot' : make_attention_dot(generate_lstm_config),
    'gru_dot' : make_attention_dot(generate_gru_config),
    'mono-lstm_dot' : make_attention_dot(generate_mono_lstm_config),
    'cnn_dot' : make_attention_dot(generate_cnn_config),
    'average_dot' : make_attention_dot(generate_average_config)
}

def wrap_config_for_qa(func) :
    def new_func(dataset) :
        config = func(dataset)
        config['model']['decoder']['attention']['type'] += '_qa'
        return config

    return new_func

configurations_qa = { k:wrap_config_for_qa(v) for k, v in configurations.items() }