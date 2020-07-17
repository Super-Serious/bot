from howlongtobeatpy import HowLongToBeat


def hltb(update, context):
    """Command to find how long a game takes to beat."""
    message = update.message
    game = ' '.join(context.args)

    if not game:
        text = "*Usage:* `/hltb {GAME_NAME}`\n"\
               "*Example:* `/hltb horizon zero dawn`"
    else:
        results = HowLongToBeat().search(game)

        if results:
            # Return result with highest similarity to query
            best_guess = max(results, key=lambda element: element.similarity)

            # check if non-zero value exists for main gameplay
            if best_guess.gameplay_main != -1:
                text = f"<b>{best_guess.gameplay_main_label}</b>: "\
                       f"{best_guess.gameplay_main} {best_guess.gameplay_main_unit}"\
                       f"<a href='{best_guess.game_image_url}'>&#8205;</a>"
            # check if non-zero value exists for main+extra gameplay
            elif best_guess.gameplay_main_extra != -1:
                text = f"<b>{best_guess.gameplay_main_extra_label}</b>: "\
                       f"{best_guess.gameplay_main_extra} {best_guess.gameplay_main_extra_unit}"\
                       f"<a href='{best_guess.game_image_url}'>&#8205;</a>"
            else:
                text = "No hours recorded."
        else:
            text = "No entry found."

    context.bot.send_message(
        chat_id=message.chat_id,
        text=text,
        parse_mode='HTML',
        disable_web_page_preview=False,
    )
