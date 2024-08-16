<template>
  <div>
   
    <div class="flex flex-row-1 gap-4 justify-center">
      <div >
        <UButton 
          style="width: 80px; 
          white-space: normal; 
          text-align: right;" 
          class="rounded-full" 
          variant="soft" 
          :onclick="reloadReport">
            Recargar
        </UButton>
      </div>
      <div >
        <UButton 
          style="width: 80px; 
          white-space: normal; 
          text-align: right;" 
          class="rounded-full" 
          variant="soft" 
          :onclick="downloadReport">
            Descargar
        </UButton>  
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-1 m-4">
      <div>
        <iframe src="http://localhost:8000/api/pdf/ambulancia/45/" width="100%" height="600px"></iframe>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>

const reloadReport = () => {
  const response = $fetch('http://localhost:8000/api/pdf/ambulancia/45/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/pdf',
    }
  }) as any
}

const downloadReport = async(value :any) => {
  console.log('Descargar')
 
  const response = await $fetch('http://localhost:8000/api/printpdf/ambulancia/45/', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/pdf',
    }
  }) as any
}

</script>

<style></style>
