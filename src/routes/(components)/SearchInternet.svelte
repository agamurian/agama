<script lang="ts">
	import Search from '$lib/components/Icons/Search.svelte';
	let query = '';
	const searchInternet = (query: string) => {
		window.location.href = 'https://duckduckgo.com/?q=' + query;
	};
	function init(el: HTMLElement) {
		el.focus();
	}
</script>

<form class="wrapper" on:submit={searchInternet(query)}>
	<div class="icon-wrapper"><Search size={30} color="#ccc6" /></div>
	<input type="text" bind:value={query} use:init />
</form>

<style lang="scss">
	.wrapper {
		display: flex;
		flex-direction: row;
		align-items: center;
		padding: 0;
		gap: 0;
		margin-left: -48px;
	}
	.icon-wrapper {
		display: flex;
		align-content: center;
		justify-content: center;
		height: 48px;
		width: 48px;
		box-sizing: border-box;
	}
	input {
		display: flex;
		align-self: center;
		box-sizing: border-box;
		background-color: #444;
		border: 3px solid #1118;
		height: 40px;
		border-radius: 20px;
		padding: 10px 20px;
		box-sizing: border-box;
		font-size: 15px;
		color: #ccc;
		outline: 3px solid #8888;
		font-family: Golos;
	}
</style>
