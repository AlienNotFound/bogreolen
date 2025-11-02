<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import type { LayoutProps, PageProps } from './$types';
	import { enhance } from '$app/forms';
	import { page } from '$app/state';
	
	let { data, children }: LayoutProps = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{#if page.url.pathname != "/login" && page.url.pathname != "/signup"}
<header>
	<a href="/">
		<h1>Bogreolen</h1>
		</a>
		<div id="menu-right">
			<a href="/user/{data.user_id}"><h2>Profile</h2></a>
			<a href="/book/create"><h2>Create a new book</h2></a>
			<form method="POST" action="/?/logout" use:enhance>
				<button type="submit">Log ud</button>
			</form>
		</div>
	</header>
{/if}

<main>
	{@render children?.()}
</main>

<style>
	:global(body) {
		font-family: Arial, Helvetica, sans-serif;
		background-color: #ccd5ae;
	}

	:global(h2, h3, h4, p) {
		margin: 0;
		line-height: 1.5;
	}

	:global(a) {
		color: #000;
		text-decoration: none;
	}

	:global(button) {
		background-color: #fefae0;
		border-radius: 5px;	
		border: none;
		padding: 8px 14px;
		font-size: 1em;
	}
	
	:global(input:focus) {
		outline: none;
    }

	:global(.error) {
		color: #bf2b24;
		font-weight: 800;
	}
	header {
		display: flex;
		justify-content: space-between;
		align-content: center;
		box-sizing: border-box;
		padding: 0 1%;
	}

	#menu-right {
		width: 15vw;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
	}

	main {
		padding: 0 1%;
	}

	/* CSS HEX
	--tea-green: #ccd5aeff;
	--beige: #e9edc9ff;
	--cornsilk: #fefae0ff;
	--papaya-whip: #faedcdff;
	--buff: #d4a373ff;

	/* CSS HSL 
	--tea-green: hsla(74, 32%, 76%, 1);
	--beige: hsla(67, 50%, 86%, 1);
	--cornsilk: hsla(52, 94%, 94%, 1);
	--papaya-whip: hsla(43, 82%, 89%, 1);
	--buff: hsla(30, 53%, 64%, 1);

	/* SCSS HEX 
	$tea-green: #ccd5aeff;
	$beige: #e9edc9ff;
	$cornsilk: #fefae0ff;
	$papaya-whip: #faedcdff;
	$buff: #d4a373ff;

	/* SCSS HSL 
	$tea-green: hsla(74, 32%, 76%, 1);
	$beige: hsla(67, 50%, 86%, 1);
	$cornsilk: hsla(52, 94%, 94%, 1);
	$papaya-whip: hsla(43, 82%, 89%, 1);
	$buff: hsla(30, 53%, 64%, 1);

	/* SCSS RGB 
	$tea-green: rgba(204, 213, 174, 1);
	$beige: rgba(233, 237, 201, 1);
	$cornsilk: rgba(254, 250, 224, 1);
	$papaya-whip: rgba(250, 237, 205, 1);
	$buff: rgba(212, 163, 115, 1);

	/* SCSS Gradient 
	$gradient-top: linear-gradient(0deg, #ccd5aeff, #e9edc9ff, #fefae0ff, #faedcdff, #d4a373ff);
	$gradient-right: linear-gradient(90deg, #ccd5aeff, #e9edc9ff, #fefae0ff, #faedcdff, #d4a373ff);
	$gradient-bottom: linear-gradient(180deg, #ccd5aeff, #e9edc9ff, #fefae0ff, #faedcdff, #d4a373ff);
	$gradient-left: linear-gradient(270deg, #ccd5aeff, #e9edc9ff, #fefae0ff, #faedcdff, #d4a373ff);
	$gradient-top-right: linear-gradient(45deg, #ccd5aeff, #e9edc9ff, #fefae0ff, #faedcdff, #d4a373ff);
	$gradient-bottom-right: linear-gradient(135deg, #ccd5aeff, #e9edc9ff, #fefae0ff, #faedcdff, #d4a373ff);
	$gradient-top-left: linear-gradient(225deg, #ccd5aeff, #e9edc9ff, #fefae0ff, #faedcdff, #d4a373ff);
	$gradient-bottom-left: linear-gradient(315deg, #ccd5aeff, #e9edc9ff, #fefae0ff, #faedcdff, #d4a373ff);
	$gradient-radial: radial-gradient(#ccd5aeff, #e9edc9ff, #fefae0ff, #faedcdff, #d4a373ff); */
</style>
