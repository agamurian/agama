<script lang="ts">
	import Settings from './Icons/Settings.svelte';
	import Modal from './Modal.svelte';
	import { bgColor } from '$lib/stores';
	import { get } from 'svelte/store';

	let modalOpened = false;
	let bgColorLocal = get(bgColor);

	$: bgColorLocal, bgColor.set(bgColorLocal);
</script>

<div
	class="set-button"
	on:click={() => {
		modalOpened = true;
	}}
>
	<Settings color="#ccc" size={20} />
</div>

<Modal bind:modalOpened>
	<div class="option">
		Background Color:
		<input
			class="picker"
			type="color"
			style="--bg-color:{bgColorLocal};"
			bind:value={bgColorLocal}
			on:change={() => {
				console.log($bgColor);
			}}
		/>
	</div>
</Modal>

<style lang="scss">
	.option {
		padding: 10px 20px;
		gap: 5px;
	}
	.picker {
		background-color: var(--bg-color);
		padding: 10px;
		margin: 15px;
		vertical-align: middle;
		width: 20px;
		height: 20px;
		border-radius: 50%;
		border: 3px solid #0004;
		outline: 3px solid #0004;
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
