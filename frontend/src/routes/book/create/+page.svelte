<script lang="ts">
    import { enhance } from "$app/forms";
    import type { PageData, ActionData } from './$types';
    let { data, form }: { data: PageData, form: ActionData } = $props();
    
    // const listMap: Record<string, string> = {
    //     "Want to read": "WANT_TO_READ",
    //     "Reading": "READING",
    //     "Finished": "FINISHED",
    //     "Didn't finish": "DIDNTFINISH"
    // };

    // // if (data.book_status) {
    // //     listval = listMap[data.book_status] ?? '';
    // // }
</script>

<h1>Create</h1>
<form action="?/create_book" method="post" use:enhance enctype="multipart/form-data">
    <h2>Title</h2>
    <input type="text" name="title">
    <h2>Author</h2>
    <input type="text" name="author_name">
    <h2>Cover</h2>
    <input type="file" name="image" />
    <h2>Summary</h2>
    <textarea name="summary" id="" rows="10"></textarea>
    <h2>Year</h2>
    <input type="text" name="year">
    <h2>Category</h2>
    <select name="category_title" id="">
        <option value="Fantasy">Fantasy</option>
        <option value="Horror">Horror</option>
    </select>
    <h2>Add to a reading list</h2>
    <select name="book_status" id="">
        <option value="">None</option>
        <option value="WANT_TO_READ">Want to read</option>
        <option value="READING">Reading</option>
        <option value="FINISHED">Finished</option>
        <option value="DIDNTFINISH">Didn't finish</option>
    </select>
    <button type="submit">Create</button>
</form>