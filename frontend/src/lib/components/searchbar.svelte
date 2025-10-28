<script lang="ts">
    type Book = {
        title: string
    }

    let searchInput = $state<string>();
    let searchSuggestions = $state<Book[]>([]);
    let showSuggestions = $state(false);

    async function fetchSearch(query: string) {
        try {
            if (query) {
                const response = await fetch('http://localhost:8000/search/' + searchInput);
                const result = await response.json()
                searchSuggestions = result;
                if (result) {
                    showSuggestions = true;
                }
                console.log(result)
            }
        } catch (err) {
            console.error(err)
        }
    }
</script>
<div>
    <input type="text"
            onkeyup={
                async (e) => {
                    searchInput = e.currentTarget.value;
                    fetchSearch(searchInput);
                    if (e.currentTarget.value == "") {
                        showSuggestions = false;
                    }
                }
            }
            >
    <button>Search</button>
    {#if showSuggestions}
        <div id="searchSuggestions">
            {#each searchSuggestions as suggestion}
                <a href="/">{suggestion.title}</a>
            {/each}
        </div>
    {/if}
</div>

<style>
    #searchSuggestions {
        display: flex;
        flex-direction: column;
    }
</style>