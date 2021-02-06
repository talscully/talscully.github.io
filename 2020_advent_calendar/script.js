function onPageLoad() {

    this_date = new Date();
    this_day = this_date.getDate();
    this_month = this_date.getMonth()+1;

    var activities = [
        /* DAY 1 */
        "Make hot cocoa.",

        /* DAY 2 */
        "Sing a carol.",

        /* DAY 3 */
        "Make paper snowflakes.",

        /* DAY 4 */
        "Reach out to someone you haven't spoken to in a while.",

        /* DAY 5 */
        "Watch a Christmas movie.",

        /* DAY6 */
        "Play a board or card game.",

        /* DAY 7 */
        "Write a letter to your future self as the ghost of Christmas past.",

        /* DAY 8 */
        "Pick a Christmas song lyric signature phrase.",

        /* DAY 9 */
        "Share a fun photo from holiday seasons past.",

        /* DAY 10 */
        "Eat dinner by candlelight. (Happy Chanukah!)",

        /* DAY 11 */
        "Research charitable donations or volunteering.",

        /* DAY 12 */
        "Create a festive cocktail.",

        /* DAY 13 */
        "Bake cookies.",

        /* DAY 14 */
        "Research future trips.",

        /* DAY 15 */
        "Decorate an unexpected spot.",

        /* DAY 16 */
        "Take a festive photo.",

        /* DAY 17 */
        "Write a Christmas haiku.",

        /* DAY 18 */
        "Watch a Christmas movie.",

        /* DAY 19 */
        "Build a gingerbread house.",

        /* DAY 20 */
        "Put together a festive outfit.",

        /* DAY 21 */
        "Turn off the lights and make a flashlight blanket fort. (Happy solstice!)",

        /* DAY 22 */
        "Send a message of gratitude.",

        /* DAY 23 */
        "Eat breakfast for dinner.",

        /* DAY 24 */
        "Make a list of 21 things to do in 2021.",
        
        /* DAY 25 */
        "Merry Christmas!",
    ];

    var visible = [5, 6, 10, 12, 13, 18, 19, 23, 25];

    /* MAKE SOME DAYS VISIBLE */
    for (i in visible) {
        iDay = visible[i];
        day_text = '#day' + (iDay) + '_text';
        day_img = '#day' + (iDay) + '_img';

        $(day_text).text(activities[iDay-1]);
        $(day_img).attr('src','images/orb_visible.png');
    }

    if (this_month == 12) {
        
        for (iDay = 0; iDay < 25; iDay++) {
                day_text = '#day' + (iDay+1) + '_text';
                day_img = '#day' + (iDay+1) + '_img';

                if (iDay < this_day) {
                    $(day_text).text(activities[iDay]);
                    $(day_img).attr('src','images/day' + (iDay+1) + '.png');
                }

        }

    }

}