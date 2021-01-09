from keyboard_mouse import create_emulator
import configargparse
import keyboard_mouse.default_config as default


def main():
    parser = get_parser()
    user_config = parse_config(parser)

    print(user_config)

    emulator = create_emulator(user_config)
    emulator.start_emulation()


def get_parser() -> configargparse.ArgParser:
    parser = configargparse.ArgParser(formatter_class=configargparse.DefaultsFormatter)
    parser.add_argument('-c', '--config', is_config_file=True, help='path to config file with ini or yaml style')
    parser.add_argument('--left', type=str, help='set key to move cursor left', default=default.left)
    parser.add_argument('--right', type=str, help='set key to move cursor right', default=default.right)
    parser.add_argument('--up', type=str, help='set key to move cursor up', default=default.up)
    parser.add_argument('--down', type=str, help='set key to move cursor down', default=default.down)
    parser.add_argument('--click', type=str, help='set key for left click', default=default.down)
    parser.add_argument('--toggle', type=str, default=default.toggle,
                        help='set key to toggle between normal (writing) mode and mouse emulation ')
    parser.add_argument('--increment', type=int, help='set mouse sensitivity in pixel per click',
                        default=default.increment)

    return parser


def parse_config(parser: configargparse.ArgParser) -> dict:
    args = parser.parse_args()
    return args.__dict__


if __name__ == '__main__':
    main()
