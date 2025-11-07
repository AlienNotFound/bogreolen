<script lang="ts">
    import { fetchGETRequest } from "$lib/api/common";
    let searchInput = $state<string>();
    let searchSuggestions = $state<Book[]>([]);
    let showSuggestions = $state(false);
    
    async function fetchSearch(query: string) {
        try {
            if (query) {
                const result = await fetchGETRequest<Book[]>('search/' + searchInput);
                searchSuggestions = result;
                if (searchSuggestions) {
                    showSuggestions = true;
                }
            }
        } catch (err) {
            console.error(err)
        }
    }

    function hideSuggestions() {
        const inputElement = <HTMLInputElement>document.getElementById("searchInput");
        if (showSuggestions) {
            showSuggestions = false;
        }

        if (inputElement) {
            inputElement.value = '';
        }
    }

</script>

<div id=searchbarwrapper>
    <input type="text"
            id="searchInput"
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
        <div id="XButton">
            <button onclick={() => hideSuggestions()}>X</button>
        </div>
        {#if showSuggestions}
        <div id="searchSuggestions">
            {#each searchSuggestions as suggestion}
            <a href="/book/{suggestion.bookid}">{suggestion.title}</a>
        {/each}
    </div>
    {/if}
</div>

<style>
    #searchbarwrapper {
        position: relative;
        display: flex;
        padding-bottom: 2%;
    }   
    #searchbarwrapper input {
        width: 100%;
        box-sizing: border-box;
        padding: 4px 10px;
        font-size: 1em;
        border: none;
    }

    #XButton button {
        background-color: #fff;
        color: #aaa;
        border-radius: 0 5px 5px 0;
    }
    #searchSuggestions {
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 60%;
        left: 0;
        background-color: #fff;
        padding: 2% 0;
        width: 25vw;
        box-sizing: border-box;
        border-radius: 0 0 5px 5px;
    }
    #searchSuggestions a {
        color: #000;
        text-decoration: none;
        padding: 4px 1%;
    }
    #searchSuggestions a:hover {
        background-color: #eee;
    }
</style>