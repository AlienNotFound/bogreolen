<script lang="ts">
    import type { Snippet } from "svelte";

    let { title, modalForm, showModal = $bindable() }: { title: string, modalForm: Snippet, showModal: boolean } = $props();

    function toggleModal() {
        showModal = !showModal;
    }
</script>

{#if showModal}
    <div id="modalWrapper">
        <div class="modal">
                <div id="modalHeader">
                    <h3>{title}</h3>
                    <button id="modalClose" onclick={() => toggleModal()}>X</button>
                </div>

                {@render modalForm()}
        </div>
    </div>
{/if}

<style>
    #modalWrapper,
    .modal,
    .books {
        display: flex;
    }
    
    .books, #modalHeader {
        justify-content: space-between;
    }

    #modalWrapper {
        position: absolute;
        top: 0;
        left: 0;
        justify-content: center;
        align-items: center;
        width: 100vw;
        height: 100vh;
        background-color: #0000003b;
    }

    #modalWrapper form {
        display: flex;
        flex-direction: column;
    }

    .modal {
		background-color: #ccd5ae;
        width: 20vw;
        height: 60vh;
        padding: 2% 3%;
        flex-direction: column;
    }

    #modalHeader {
        flex-direction: row;
        display: flex;
        align-items: center;
    }

    .books {
        flex-direction: column;
        padding: 2% 3%;
        width: 100%;
        height: 100%;
    }

    .books img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }

    input {
        margin-bottom: 4%;
        /* height: 2vh; */
        padding: 1% 2%;
        font-size: 1em;
    }
</style>