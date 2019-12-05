import pytest_mock
from tictactoe_user_handler import TicTacToeUserHandler


def test_tictactoeuserhandler_winx(mocker: pytest_mock.MockFixture) -> None:
    send_message = mocker.stub(name='send_message_stub')
    bot = TicTacToeUserHandler(send_message)
    bot.handle_message('start')
    bot.handle_message('X 1 1')
    bot.handle_message('O 2 0')
    bot.handle_message('O 1 0')
    bot.handle_message('X 1 0')
    bot.handle_message('O 0 2')
    bot.handle_message('X 1 2')
    assert send_message.call_args_list == [
        mocker.call('...\n...\n...'),
        mocker.call('...\n.X.\n...'),
        mocker.call('..O\n.X.\n...'),
        mocker.call('Invalid turn'),
        mocker.call('.XO\n.X.\n...'),
        mocker.call('.XO\n.X.\nO..'),
        mocker.call('.XO\n.X.\nOX.'),
        mocker.call('Game is finished, X wins'),
    ]


def test_tictactoeuserhandler_wino(mocker: pytest_mock.MockFixture) -> None:
    send_message = mocker.stub(name='send_message_stub')
    bot = TicTacToeUserHandler(send_message)
    bot.handle_message('start')
    bot.handle_message('X 0 0')
    bot.handle_message('O 2 0')
    bot.handle_message('O 1 0')
    bot.handle_message('X 1 0')
    bot.handle_message('O 2 1')
    bot.handle_message('X 1 1')
    bot.handle_message('O 2 2')
    assert send_message.call_args_list == [
        mocker.call('...\n...\n...'),
        mocker.call('X..\n...\n...'),
        mocker.call('X.O\n...\n...'),
        mocker.call('Invalid turn'),
        mocker.call('XXO\n...\n...'),
        mocker.call('XXO\n..O\n...'),
        mocker.call('XXO\n.XO\n...'),
        mocker.call('XXO\n.XO\n..O'),
        mocker.call('Game is finished, O wins'),
    ]


def test_tictactoeuserhandler_draw(mocker: pytest_mock.MockFixture) -> None:
    send_message = mocker.stub(name='send_message_stub')
    bot = TicTacToeUserHandler(send_message)
    bot.handle_message('start')
    bot.handle_message('X 0 0')
    bot.handle_message('O 2 0')
    bot.handle_message('O 1 0')
    bot.handle_message('X 0 2')
    bot.handle_message('O 0 1')
    bot.handle_message('X 1 1')
    bot.handle_message('O 2 2')
    bot.handle_message('X 2 1')
    bot.handle_message('O 1 0')
    bot.handle_message('X 1 2')
    assert send_message.call_args_list == [
        mocker.call('...\n...\n...'),
        mocker.call('X..\n...\n...'),
        mocker.call('X.O\n...\n...'),
        mocker.call('Invalid turn'),
        mocker.call('X.O\n...\nX..'),
        mocker.call('X.O\nO..\nX..'),
        mocker.call('X.O\nOX.\nX..'),
        mocker.call('X.O\nOX.\nX.O'),
        mocker.call('X.O\nOXX\nX.O'),
        mocker.call('XOO\nOXX\nX.O'),
        mocker.call('XOO\nOXX\nXXO'),
        mocker.call('Game is finished, draw'),
    ]
