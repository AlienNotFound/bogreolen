<script lang="ts">
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
<div id="searchbar">
    <div id=searchbarwrapper>

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
                style="border-radius: {showSuggestions ? '5px 0 0 0' : '5px 0 0 5px'}"
                    
            >
            <button>Search</button>
            {#if showSuggestions}
            <div id="searchSuggestions">
                {#each searchSuggestions as suggestion}
                <a href="/book/{suggestion.bookid}">{suggestion.title}</a>
            {/each}
        </div>
        {/if}
    </div>
</div>

<style>
    #searchbarwrapper {
        position: relative;
        display: flex;
        padding-bottom: 2%;
    }   
    #searchbar {
        width: 100vw;
        display: flex;
        justify-content: center;
    }

    #searchbar input {
        width: 25vw;
        box-sizing: border-box;
        padding: 4px 10px;
        font-size: 1em;
        border: none;
    }

    #searchbar button {
        border-radius: 0 5px 5px 0;
        width: 6vw
    }
    #searchSuggestions {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 48%;
        left: 0;
        background-color: #fff;
        padding: 1%;
        width: 25vw;
        box-sizing: border-box;
        border-radius: 0 0 5px 5px;
    }

    #searchSuggestions a {
        color: #000;
        text-decoration: none;
        padding: 4px 0;
    }

    #searchSuggestions a:hover {
        background-color: #eee;
    }
</style>