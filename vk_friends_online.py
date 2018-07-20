import vk
from getpass import getpass


APP_ID = 6636679


def get_user_login():
    login = input("Input your username: ")
    return login


def get_user_password():
    password = getpass("Input your password: ")
    return password


def get_online_friends(login, password, version_api=5.80):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends",
    )
    api = vk.API(session, v=version_api)
    friends_online = api.users.get(
        user_ids=api.friends.getOnline()
    )
    return friends_online


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print("{} {}".format(friend["first_name"], friend["last_name"]))


if __name__ == "__main__":
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkException:
        exit("Error: you input incorrect login or password!")
    output_friends_to_console(friends_online)
