<script lang="ts">
	import Close from '$lib/components/Icons/Close.svelte';
	export let modalOpened = false;
</script>

{#if modalOpened}
	<div class="bg">
		<div class="modal">
			<slot />
		</div>
	</div>
	<div
		class="set-button"
		on:click={() => {
			modalOpened = false;
		}}
	>
		<Close color="#ccc" size={20} />
	</div>
{/if}

<style lang="scss">
	.bg {
		position: fixed;
		background-color: #3333;
		top: 0;
		left: 0;
		width: 100vw;
		height: 100vh;
		backdrop-filter: blur(10px);
	}
	.modal {
		position: fixed;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		background-color: #3d3d3d;
		border-radius: 0px;
		overflow-x: hidden;
		overflow-y: scroll;
		height: 50vh;
		width: 50vw;
	}
	.set-button {
		position: fixed;
		border-radius: 10px;
		height: 40px;
		width: 40px;
		top: 20px;
		right: 20px;
		background-color: #444;
		display: flex;
		justify-content: center;
		cursor: pointer;
		&:hover {
			background-color: #8a3434;
		}
	}
</style>
