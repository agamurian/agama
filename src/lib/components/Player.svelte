<script lang="ts">
	import Play from './Icons/Play.svelte';
	import Modal from './Modal.svelte';

	let modalOpened = false;
</script>

<div
	class="play-button"
	on:click={() => {
		modalOpened = true;
	}}
>
	<Play color="#ccc" size={20} />
</div>

<Modal bind:modalOpened>
	<div class="option">
		player
	</div>
</Modal>

<style lang="scss">
	.option {
		padding: 10px 20px;
		gap: 5px;
	}
	.play-button {
		position: fixed;
		border-radius: 10px;
		height: 40px;
		width: 40px;
		top: 20px;
		left: 20px;
		background-color: #444;
		display: flex;
		justify-content: center;
		cursor: pointer;
		&:hover {
			background-color: #8a3434;
		}
	}
</style>
