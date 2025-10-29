type Day = {
    name: string;
    date: string;
    raw_date: Date;
    isToday: boolean;
};

type Track = {
    book_id: number,
    title: string,
    book_status: string,
    date: string
}

type Book = {
    book_id: number,
    title: string,
    image: string,
    book_status: string
}