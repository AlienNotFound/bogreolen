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

type Review = {
    bookid: number,
    title: string,
    rating: number,
    username: string,
    review: string
}

type Book = {
    book_id: number,
    title: string,
    image: string,
    book_status: string
}

type BookDetails = {
    bookid: number,
    title: string,
    author_name: string,
    image: string,
    summary: string,
    year: number,
    average_rating: number,
    reviews: Review[],
    category_title: string,
    book_status: string
}