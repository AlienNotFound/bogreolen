<script lang="ts">
    let { modalInfo, selectedDate, showModal = $bindable() }: { modalInfo: Track | null, selectedDate: string, showModal: boolean } = $props();
    let formData: Record<number, {current_page: number, last_page: number, error_message: string}> = {};
    const infoDate = new Date(modalInfo!.date).toISOString().split('T')[0]

    function toggleModal() {
        showModal = !showModal;
    }
</script>

<div id="modalWrapper">
    <div class="modal">
        {#if modalInfo}
            <div id="modalHeader">
                <h3>{modalInfo.title}</h3>
                <button id="modalClose" onclick={() => toggleModal()}>X</button>
            </div>

            <div class="books">
                <img src={modalInfo.image} alt="Book cover">
            </div>
            <form method="POST" action="?/edit_track">
                <input type="text" name="track_id" value={modalInfo.track_id} hidden>
                <h4>Date:</h4>
                <input type="date" name="date" value={infoDate} required>
                <h4>Current page:</h4>
                <input type="number"
                name="current_page"
                value={modalInfo.current_page}
                required>
                <h4>Last page:</h4>
                <input type="number"
                name="last_page" 
                value={modalInfo.last_page}
                required/>
                <button>Mark as read</button>
            </form>            
        {/if}
    </div>
</div>

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