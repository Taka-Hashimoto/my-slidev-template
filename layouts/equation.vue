<template>
  <SlideFrame>
    <div class="plain-equation"><slot /></div>
    <template v-if="$slots.takeaway" #takeaway><slot name="takeaway" /></template>
    <template v-if="$slots.note" #note><slot name="note" /></template>
  </SlideFrame>
</template>
