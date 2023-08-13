<script lang="ts">
	import Search from '$lib/components/Icons/Search.svelte';
  let query = '';
  let g = '';
  const toggle_g = () => {g == '' ? g = '!g ' : g = ''}
	const searchInternet = (query: string) => {
		window.location.href = 'https://duckduckgo.com/?q=' + g + query;
	};
	function init(el: HTMLElement) {
		el.focus();
  }
  let width = 240

</script>

<form class="wrapper" on:submit={searchInternet(query)}>
  <div class="icon-wrapper" style="cursor:pointer" on:click={searchInternet(query)}>
    <Search size={30} color="#ccc6" />
  </div>
  <input type="text" 
    bind:value={query} 
    use:init 
    style='width: {width}px' 
    on:focus={() => {width = 360}}
    on:blur={() => { setTimeout(() => {width = 240}, 10000) }}/>
    <div class="icon-wrapper" on:click={toggle_g}>
      {#if g==''}
        <img src="/duck.svg" width="22" height="22" alt="google" />
      {:else}
        <img src="/google.svg" width="22" height="22" alt="google" />
      {/if}
    </div>
</form>

<style lang="scss">
	.wrapper {
		display: flex;
		flex-direction: row;
		align-items: center;
		padding: 0;
	}
	.icon-wrapper {
		display: flex;
		align-content: center;
		justify-content: center;
		height: 48px;
		width: 48px;
    box-sizing: border-box;
    transition: 0.2s ease;
    opacity: 0.35;
      &:hover {
        opacity: 1.0;
      }
	}
	input {
    transition: 0.2s ease-out;
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
    margin: 0 5px;
  }
  img {
    opacity: 0.7;
    margin: auto;
    transition: 0.2s ease;
    filter: grayscale(1.0);
      &:hover {
        filter: grayscale(0.1);
      }
  }
</style>
