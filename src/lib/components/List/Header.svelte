<script lang="ts">
	import Plus from '$lib/components/Icons/Plus.svelte';
	export let title = '';
	export let plusClick = () => {};
</script>

<div class="content">
	<div class="icon-wrapper" on:click={() => plusClick()}><Plus /></div>
	<div class="title">{title}</div>
</div>

<style lang="scss">
	.content {
		display: flex;
		background-color: #181818;
		color: #dcdcdc;
		margin: 0px;
		border-top-right-radius: 0px;
		border-top-left-radius: 0px;
	}
	.icon-wrapper {
		display: flex;
		align-content: center;
		justify-content: center;
		aspect-ratio: 1;
		background-color: #545454;
		border-top-left-radius: 0px;
		cursor: pointer;
		&:hover {
			background-color: #8a3434;
		}
	}
	.title {
		font-weight: 700;
		padding: 10px 15px;
		text-transform: capitalize;
	}
</style>
