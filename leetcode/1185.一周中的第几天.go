func dayOfTheWeek(day, month, year int) string {
    t := time.Date(year, time.Month(month), day, 0, 0, 0, 0, time.UTC)
    return t.Weekday().String()
}