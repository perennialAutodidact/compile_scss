import click
from src.utilities import valid_path
import re

def set_config_file(options, config_loaded = False):
    '''
    Read, Evaluate, Print, Loop allowing the user to set 
    new option values and generating a JSON config file or 
    to return the default values set within compile_scss
    '''

    menu_options = {
        '1': 'Change configuration file',
        '2': 'Use current configuration',
        '3': 'Exit',
    }

    click.echo("-"*23)
    click.echo("Configure Compile SCSS")
    click.echo("-"*23+"\n")

    if not config_loaded:
        click.echo(f"No configuration file was found in the current root directory: {options['root']}\n")

    if options != {}:
        click.echo("Your current configuration:")
        for key in options.keys():
            click.echo(f"-{key}: {options[key]}")
        
    while True:
        click.echo("\nPlease choose from the following options: \n")
    
        #  display each menu option with it's message
        for number in menu_options.keys():
            click.echo(f"{number}. {menu_options[number]}")

        choice = click.prompt("\nEnter the number of your selection")
        if choice not in menu_options.keys():
            invalid_entry(choice, 'selection')
            continue
        elif choice == "1":
            #  ask user for a value for each config option
            options = prompt_for_options(options)
            break
        elif choice == "2":
            break
        elif choice == "3":
            click.echo("Goodbye!")
            exit()

    return options


def prompt_for_options(options):
    '''
    REPL that prompts user for a value for each option,
    if they choose to override the default options.
    '''
    
    prompts = {
        'root': {
            'msg': "the path to your SCSS directory"
        },
        'css_dir': {
            'msg': "the path to your target CSS directory"
        },
        'css_filename': {
            'msg': "the file name you'd like for your CSS file"
        },
        'output_style': {
            'msg': "the output style of your CSS",
            'options': ['compact', 'compressed', 'expanded', 'nested']
        }
    }

    filename_regex = r'[^\WA-Z0-9\-_][a-z-]+'

    while True:
        click.echo("")
        for key in options.keys():
            while True:
                prompt_message = prompts[key]['msg']
                user_entry = click.prompt(f"Please enter {prompt_message}")
                
                options[key] = user_entry
                # if prompt is for a directory path, 
                # check that the directory exists
                if 'path' in prompt_message:
                    if not valid_path(user_entry):
                        invalid_entry(user_entry, 'path')
                        continue
                    else:
                        break  # break SCSS/CSS directory loops

                # receive user value for CSS file name
                # and ensure its validity.
                elif 'file name' in prompt_message:
                    default_filename = 'index'
                    regex_match = re.match(filename_regex, user_entry)
                    if regex_match:
                        regex_match = regex_match.group()
                    else:
                        regex_match = ''

                    if not len(regex_match) == len(user_entry) or user_entry[-1] == '-':
                        invalid_entry(user_entry, 'file name')
                        click.echo(
                            f"For the sake of simplicity, please make your file name a single,\nlowercase word with no numbers or punctuation (except non-leading hyphens).\nThe default is '{default_filename}'and the file extension '.css' will be added automatically.\n"
                        )
                        continue
                    else:
                        click.echo("VALID FILENAME")
                        break  # break file name loop

                # if the prompt has additional options,
                # ensure that input is on of them
                elif 'options' in prompts[key].keys():
                    if options[key] not in prompts[key]['options']:
                        invalid_entry(user_entry, 'output style')

                        click.echo(f"Enter one of these: {', '.join(prompts[key]['options'])}\n")
                    else:
                        break  # break output_style options loop
                else:
                    break  # break while loop for current key
        return options

def invalid_entry(entry, option_type):
    '''
    Display an error message in the config REPL if an invalid entry is provided by ther user.
    "Your entry: '{entry:str}' is not a valid {option_type:str}."
    '''
    error = f"Your entry: '{entry}' is not a valid {option_type}."
    click.echo('\n' + '!'*(len(error) + 2))
    click.echo(f" {error} ")
    click.echo('!'*(len(error) + 2) + '\n')