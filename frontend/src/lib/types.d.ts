type Day = {
    name: string;
    date: string;
    raw_date: Date;
    isToday: boolean;
};

type Track = {
    book_id: number,
    track_id: number,
    title: string,
    image: string,
    book_status: string,
    date: Date,
    current_page: number,
    last_page: number
}

type Review = {
    review_id: number,
    book_id: number,
    user_id: number,
    title: string,
    rating: number,
    username: string,
    review: string,
    comments: ReviewComment[];
}

type Book = {
    book_id: number,
    bookid: number,
    title: string,
    image: string,
    book_status: string
}

type BookDetails = {
    bookid: number,
    book_id: number,
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

type User = {
    userid: number,
    username: string,
    email: string
}

type ReviewComment = {
    comment_id: number,
    comment_text: string,
    user_id: number,
    username: string,
}

type ResponseMessage<T> = {
    Error: string,
    Success: string,
    status: number,
    msg: string,
    ok: boolean,
    data: T | null;
}

type LayoutData = {
    token: string | null;
}