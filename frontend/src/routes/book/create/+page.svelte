<script lang="ts">
    import type { PageData, ActionData } from './$types';
    let { data, form }: { data: PageData, form: ActionData } = $props();
    import { enhance } from "$app/forms";
    console.log(form);
    
</script>

<svelte:head>
  <title>Create new book</title>
</svelte:head>

<h1>Create</h1>
<form action="?/create_book" id="createBookForm" method="post" enctype="multipart/form-data" autocomplete="off" use:enhance={() => {
  return async ({ update }) => {
    update({ reset: false });
  }
}}>
    <h2>Title</h2>
    <input type="text" name="title" required />

    <h2>Author</h2>
    <input name="author_name" list="author_list" required />
    <datalist id="author_list">
        {#if data.authors}
            {#each data.authors as author}
                <option value={author.name} />
            {/each}
        {/if}
    </datalist>

    <h2>Cover</h2>
    <!-- <input type="file" name="image" required /> -->

    <h2>Summary</h2>
    <textarea name="summary" id="" rows="10" required></textarea>
    <h2>Year</h2>
    <input type="text" name="year" required />

    <h2>Category</h2>
    <input name="category_title" list="category_list" required />
    
    <datalist id="category_list">
        {#if data.categories}
            {#each data.categories as category}
                <option value={category.title} />
            {/each}
        {/if}
    </datalist>
    
    <h2>Add to a reading list</h2>
    <select name="listname" id="">
        <option value="">None</option>
        <option value="WANT_TO_READ">Want to read</option>
        <option value="READING">Reading</option>
        <option value="FINISHED">Finished</option>
        <option value="DIDNTFINISH">Didn't finish</option>
    </select>
    <button type="submit">Create</button>

    {#if form?.error}
    <div class="error">
        <p>{form.error}</p>
    </div>
    {:else if !form?.error}
    <div class="success">
        <p>{form}</p>
    </div>
    {/if}
</form>

<style>
    #createBookForm {
        display: flex;
        flex-direction: column;
        width: 25vw;
    }

    #createBookForm input, #createBookForm select {
        margin-bottom: 2%;
    }
</style>