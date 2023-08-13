<script lang="ts">
	export let content = '';
	function init(el: HTMLElement) {
		el.focus();
	}
</script>

<div contenteditable="true" class="content f-500">{content}</div>

<style lang="scss">
	.content {
		background-color: #666;
		color: #eee;
		padding: 10px;
		margin: 0px;
		&:focus {
			outline: 5px solid #eee3;
		}
	}
</style>
