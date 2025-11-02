const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

export function getCurrentWeek() {
        const today = new Date();

        const firstDayOfWeek = new Date(today);
        const day = today.getDay();
        const diff = (day === 0 ? -6 : 1) - day;
        firstDayOfWeek.setDate(today.getDate() + diff);

        const result: Day[] = [];

        for (let i = 0; i < 7; i++) {
        const d = new Date(firstDayOfWeek);
        d.setDate(firstDayOfWeek.getDate() + i);

        result.push({
            name: days[i],
            date: d.toLocaleDateString("en-US", { month: "short", day: "numeric" }),
            raw_date: d,
            isToday:
            d.toDateString() === today.toDateString(),
            });
        }

        return result;
}

export function trackerCalendarCells() {
    const today = new Date();
	const month = today.getMonth();
	const year = today.getFullYear();
	const daysInMonth = new Date(year, month + 1, 0).getDate();
	const startDay = new Date(year, month, 1).getDay();
	const calendarCells: (Date | null)[] = [];

    for (let i = 1; i < startDay; i++) {
		calendarCells.push(null)		
	}
	
	for (let day = 1; day <= daysInMonth; day++) {
		const currentDate = new Date(year, month, day);
		calendarCells.push(currentDate)		
	}

    return calendarCells;
}

export function formatDate(d: any) {
    return new Date(d).toISOString().split('T')[0];
}

export function matchTrackToDate(day: any, tracks: Track[]) {
    const seen = new Map();
    return tracks.filter(t => 
        formatDate(t.date) === formatDate(day)
    ).filter(t => {
        if (seen.has(t.book_id)) return false;
        seen.set(t.book_id, true)
        return true;
    })
}