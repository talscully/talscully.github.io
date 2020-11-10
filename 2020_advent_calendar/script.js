function onPageLoad() {

    this_date = new Date()
    this_day = this_date.getDate()
    this_month = this_date.getMonth()+1

    var activities = [
        /* DAY 1 */
        'Day 1 text placeholder.',
    ]

    if (this_month == 12) {
        for (iDay = 0; iDay < this_day; iDay++) {
            day_text = '#day' + (iDay+1) + '_text'
            day_img = '#day' + (iDay+1) + '_img'
            $(day_text).text(activities[iDay])
            $(day_img).attr('src','images/day' + (iDay+1) + '.png')
        }
    }

}