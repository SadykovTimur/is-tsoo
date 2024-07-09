def pytest_addoption(parser):
    group = parser.getgroup('is-tsoo')

    group.addoption(
        '--browser', dest='browser', metavar='browser', default='chrome', help='Browser. Default option is chrome'
    )

    group.addoption(
        '--ui_url',
        help='A way to override the ui_url for your tests.',
        metavar='ui_url',
        default='tsoo.mos.ru',
    )

    parser.addoption(
        '--remote_ip',
        help='A way to set remote url of selenoid',
        dest='remote_ip',
        metavar='remote_ip',
        default='selenoid1.kdc',
    )

    parser.addoption(
        '--remote_port',
        help='A way to set remote port of selenoid',
        dest='remote_port',
        metavar='remote_port',
        default='4444',
    )

    parser.addoption(
        '--remote_ui',
        help='A way to set remote url of selenoid ui',
        dest='remote_ui',
        metavar='remote_ui',
        default='selenoid1.kdc',
    )

    parser.addoption(
        '--wait',
        help='(int) Value waiting of condition in seconds',
        dest='wait',
        metavar='wait',
        type=int,
        default=30,
    )

    parser.addoption(
        '--enable-video',
        action='store',
        dest='enable_video',
        type=bool,
        default=False,
        help='Enable recording video option',
    )

    parser.addoption(
        '--block-urls',
        action='store',
        dest='block_urls',
        type=bool,
        default=False,
        help='Block request urls',
    )

    parser.addoption(
        '--user_d', action='store', dest='username_d', type=str, default='mon_dispatcher', help='Username_d'
    )
    parser.addoption('--password_d', action='store', dest='password_d', type=str, default='c9PZil4H', help='Password_d')
    parser.addoption(
        '--user_l', action='store', dest='username_l', type=str, default='mon_inspector', help='Username_l'
    )
    parser.addoption('--password_l', action='store', dest='password_l', type=str, default='jc#Ho%Oq', help='Password_l')
    parser.addoption(
        '--user_dog', action='store', dest='username_dog', type=str, default='mon_agreemenet', help='Username_dog'
    )
    parser.addoption(
        '--password_dog', action='store', dest='password_dog', type=str, default='FEC2fEW8', help='Password_dog'
    )
    parser.addoption(
        '--user_ab', action='store', dest='username_ab', type=str, default='mon_abonent', help='Username_ab'
    )
    parser.addoption(
        '--password_ab', action='store', dest='password_ab', type=str, default='sGHiLyV#', help='Password_ab'
    )
    parser.addoption(
        '--user_api', action='store', dest='username_api', type=str, default='mon_dispatcher', help='Username_api'
    )
    parser.addoption(
        '--password_api', action='store', dest='password_api', type=str, default='c9PZil4H', help='Password_api'
    )
