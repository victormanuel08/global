<template>
  <UModal v-model="innerShow">
    <div class="camera-modal border rounded">
      <div class="camera-container">
        <!-- Video o imagen principal -->
        <div class="camera-video">
          <video ref="cameraVideoEl" autoplay></video>
        </div>

        <!-- Botones al lado derecho de la imagen -->
        <div class="buttons-right">
          <button class="round-button large-icon" @click="toggleCamera">
            <span class="icon">🔄</span>
          </button>
          <button class="round-button large-icon" @click="takePhoto">
            <span class="icon">📷</span>
          </button>
          <button class="round-button large-icon" @click="addDefaultThumbnail">
            <span class="icon">🌟</span>
          </button>

          <!-- Input para subir archivo de imagen -->
          
          <input ref="fileInput" type="file" accept="image/*" @change="uploadPhoto" class="hidden" />
          <UButton variant="soft" @click="triggerFileInput" class="round-button large-icon">
            📁
          </UButton>
        </div>
      </div>

      <div class="captured-photos">
        <!-- Mostrar las miniaturas de las fotos seleccionadas -->
        <div v-for="(photo, index) in capturedPhotos" :key="index" class="photo-item"
          :class="{ selected: selectedPhotos.includes(index) }" @click="togglePhotoSelection(index)">
          <img :src="photo || defaultThumbnail" alt="Captured" />
        </div>
      </div>

      <!-- Botones de guardar y unir en la parte inferior -->
      <div class="save-merge-buttons">
        <button class="round-button large-icon save-btn" @click="confirmPhoto">
          <span class="icon">💾</span>
        </button>
        <button class="round-button large-icon merge-btn" @click="mergePhotos">
          <span class="icon">🔗</span>
        </button>
      </div>
    </div>
  </UModal>
</template>

<script setup lang="ts">
const props = defineProps({ record: Object, detail: Boolean, typeImg: String });
const innerShow = defineModel<boolean>();
const cameraVideoEl = ref<HTMLVideoElement>();
const currentCamera = ref<'user' | 'environment'>('environment');
const capturedPhotos = ref<string[]>([]); // Almacena fotos capturadas
const selectedPhotos = ref<number[]>([]); // Índices de fotos seleccionadas
const selectedPhotoToSend = ref<string | null>(null);

const fileInput = ref<HTMLInputElement | null>(null);

const triggerFileInput = () => {
  fileInput.value?.click();
}


// Miniatura por defecto en Base64
const defaultThumbnail =
  'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAeAB4AAD/4QAiRXhpZgAATU0AKgAAAAgAAQESAAMAAAABAAEAAAAAAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCACPARYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9/KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKK+Yv8AgrL/AMFBrv8A4JpfstW/xEsfCkXjK7vPENhoEOnS3/2JC90zKHMmx8AFR271598KP+Crvizwv+1x4a+Dnx8+FUHws1zx7p8uo+FdW0/X01jStVEMZkmhMvlxskqqCdpX+YoA+3qK/OO8/wCC4Xjrxz8NPGnxb+G/wBv/ABl8B/AOoXFpqPiOTX47TUr+G1kK3V1aWRjbzIo8Mcs6n5G44r0X4vf8FidNu7v4S+Gvgl4Nuvi38QfjPog8TaJpX25NOtbDS8gNd3k7BvLQHcvCsSykUAfa9FfEXxL/AOCnvxI/Z18VfBTw38TfhFpXh7xJ8XfGj+FjBYeJRf29jCI1dLpJREvmZyQUIXBB5ra+MP8AwVQk+Ff7W3xk+GA8HLeL8J/hq/xAF+b8odRKxNJ9m2bDs+7jfk9elAH2HRX51fsZf8F/tB/ab/4J8/Fz416/4P8A+EP1P4Slxd+H21Dznu98SNaFZCikCd5FjB29c4zXB+Hv+DjbWfFf/BPbQfjVafCG1j1nxB8Ql8AQ6Bc6+YY4pWO1ZnnMPyjcQCCnHPNAH6o0V+dn7av/AAWb+I//AAT7/ZP0H4ifEb4OeHZtW1/xWmgwaR4e8Xf2ohtmhD+eJVgGZN29fK29gc813/i7/gsFpd78Yv2aPDngPw9aeLdM/aSsdQu9O1F9S+zjTntrN7gROuxskunltkgqc8HGKAPtSivzu8I/8FVv2i/E37bOtfAyT9nzwNbeKfDWk22v6pKfiDm2hsJmAEiv9k+ZwDnbx9aL3/gtd48+J2g/Ebxv8H/gRc/ED4S/Ce+msNd16fX00+91B7Y5u20+1MbGdYk5yWXcQQOeKAP0Roryz4IftX+G/wBo79k7Svi74QaS+8P63oba1aRyjy5MLGzGJx/CwZSp9CDXyp+w/wD8FYPi9+19+zfe/Gi4+CvhrQPhbBpWrX8N8njA3F/LLYmVfKNt9nXAd4mG7dwMHBoA+/qK/Nx/+C9+oeKvhx+ztF4R+GFnqfxH/aHtLi/07SdS8RJpumadDBv3+ZePGcsdnyqEyc16f4//AOCnPjr4E+PP2fPCPxD+FVl4f8VfGrxLfeH7y1ttfF5Bo6wbzHcRyrGBMsiKrAEIQG55FAH2pRXwv4e/4Kr/ABD/AGoPi7450f8AZ1+Ddr8R/CXw41V9D1fxNrHiVNFtbu+jx5sVmnlSNLsz1O0Hj1qz8Qf+CqXjvxf+0b4t+FvwN+EEPxM8SfDPT4bnxlPfeIU0mx0y6kj3ixhkMbmaccgjAGQeeKAPt+ivAf8AgnX+354b/wCCiXwDbxloWn6hoOoaZqE+i67ot8R9p0e/gO2WByOCBwQw6gg188/sX/8ABePQP2p/2uvjD8HdV8K/8Il4g+HM2oLossl+ZYvEyWTMJghKKFkUbGKAsdrE9qAP0Eor85fBf/BwFp3i39i34d/ECL4dX178Qvi14pv/AAj4T8GWN+JDfXVtdSW/mSXDIBHF8gZmK/KGPXFetfszf8FLfEvib9sKf4CfGb4bRfC74kXWjf8ACQaH9i1ldX0vXbMECTyrgRx4lRiQyFc/KSMjmgD7AooooAKKKKACiiigAooooAKKKKACiiigAory/wAd/tq/Bz4WeL7jw/4n+LPwy8N69ZlVn03VPFFjZ3kJYAqGiklV1yCCMjkEV03iT41eDPBdlodxrHi3wzpVt4luY7LSJbzVIIU1WeQgRxW5ZgJXYkbVTJOeBQB8ef8ABw1+zN8Qv2rv2CtO8O/DPwpe+MvEth410fWW020nhhle3t5HaRg0zonAI79682u/2Y/jN/wUx/bv+FPj74ifDDUvgp8N/gppt/HaWer6paXmra9f3doYCwW2d0jhQNkHdklOnNfefjv9rL4WfC3xlD4c8T/EzwB4c8Q3JQRaXqniKzs72XedqbYZJA53HgYHJ6VR8TftsfBrwP4zl8N6z8W/hlpHiK3lW3l0u98U2NvexyNjajQvKHDHIwCMnIoA/NL4NfAL9qb9i/8AYK8d/sk6J8EG8cxa2+r6T4c8ewa7ZwaPFYam8paa7jd1nWWJZn+VUYEhevNbmk/8E1vi9/wTK+OH7P8A8Uvhh4UPxntfAXw5T4c+K/D9pfQ2eoOPMeX7ZatOyxkB2wVZhwPfj9M/id8e/A3wR0K21Txl408J+EdNvGCQXetavb2EE7EZAV5XVWJHoai1X9oXwBoPwyi8aX/jjwhZ+DZwhj16fWbaPTJA5wuLkuIjuPAw3NAHwX+3x8Kfjh+218Pfgr8YNE+DWpeHPGfwV+IC69/wgmr6vZnUdX09QI3KTRuYFlPJVS+MYyR0rB0T9k74z/tP/GH9qn43+J/hjf8Aw6vPH/wum8CeE/Cl9qNrc6neSraSL5kjRO0Sb5CFX5+h5xjNfo54h+NvgzwjZaFdat4u8L6Xa+KZ47XRZrvVYII9Xmkx5cduzMBM75G1UyTkYzWdqf7Tnw30TTfEV7d/EHwRa2fhC4W016ebXbWOLRJmICxXTF8QOSQAsm0kmgD8b9B/4IpfGofE/wDZ90e28PS6N8NvGXhzQH+MNr9ogItb/RN0kUUiiQ7/ADtsMZ2BhwxJHWsfxv8A8EpPjo3/AAS6i8Dy/B7Vdf1i2+PM/i248OR31ksl9opmZt4ZphHh04wWDc8gV+0fw5/ar+F/xgs9TuPCPxJ8BeKYNFi+0ajJpHiC0vksI8E75TFIwjXAJy2Bwa29O+L/AIS1j4cN4xtPFHh268Ii3e7OuRalC+miBM7pftAby9i4OW3YGDzQB+VP7Sn7Eniz47/s7/BXQfhl+y1rvwg0/wAH/GDTNd1nw/d3+nyb7NPLM99+7uHUpgbSudx2n5az9P8A+CQXxb/Zx/4LjfBnxL4K0q71j9m7QNa1bxNBi4hVPBlxf2NwlxahGcSGJpyjKEVgPMPua/Ur4U/tV/C748avcad4G+JXgHxlf2kXnz22heILTUZoY843skMjFVzxkjFRfFD9rv4T/A/xGujeNPif8PPB+rtEs4sdb8R2en3JjOcP5csittODg4xxQB8w+CP2UfHMP/Bcb4rfEy+8P3Vv8OvE3w4sNCs9a86Ixz3SECSIIG8wFRnkqB7185/Af4EftO/8E6/2cPiz+zx4c+CcvxO0/wAYarqc/hHxlY61Z22m2cGpOwJ1COWRZlaIuzkRq2RgCv1B0n48eB9e8cQ+GbHxn4VvfEtzZrqUOkwavbyX0tqwDLcLCHLmIhgQ4G0gjnmr3hb4qeF/HPiLWdI0TxJoOsar4cmFtq1lY6hFcXGlynOI540YtExweHAPBoA8I/Ya/Yw1D9jD/gmh4e+ED3Mesa5onhu5tbiSE4juLyZJHcJnovmOQM9q+Qv+CT3/AASJ1v8AZr/4JnaxceJvD/jTR/jXq/h3xFpEug3PieafT8XMs/kBLRZ2tEd08ohwAQWJJBJr9CPHf7ZXwh+FvjWTw34n+K3w28OeIoCgl0vVPE1lZ3sZcAoDDJKHG4EEZHIIx1rqtA+Kvhbxf4s1LQNL8SaDqeu6MkcuoadaahDNd2KSANG0sSsXjDAgqWAyDkUAfk3cfsPeI7X/AIJW/BX4R/En9kvxV8VPEeheG51W80XXbCw1PwfqAmJQCZp0K7htOY3YEAgjmqvwy/4Jv/tN2Phz9hyH4hWep+LtU+GPi7UtQ8R3UmqQ3U3h3TJkcW0U0zMDMyIyoSgbGMdBX62/E34ueFPgp4YOt+MvE/h7wloyyrAb/WtRhsLUSNnanmSsq7jg4GcnBqp4o+PPgfwR8OrfxhrXjPwno/hO7EbQa3fatb2+nTCTmMrcO4jYN2w3PagD85v2Gvhp+0H/AMEg9d+Jnw4svgfrXxn8E+KfFl34o8O+I/D2r2Nr5C3bDdBdx3EqMrIVzlQ3B78CtDwP8GPjv/wTT/bg+O3xA8G/B3U/jJ4R/aAuofEiQ6TrFna3vh/VNhMlvOLh0DQb3YBkJOAOM1+hPif48+BvBPw9t/F2s+NPCekeFLyNJYNavdXt7fTpkfGxlndxGwbIwQ3ORimaH+0F4C8UfDSfxrpvjbwjqHg60R5J9dttYt5tMhVDh2a4VzEApBBJbg0AfMn/AARV/YS8XfsSfs+eLJviC1hF44+J3iu98YatYWMvm2+ktcFdtsr9HKKoyw7k44Ar4u8Nf8EYvij45+Dn7ROs/wBiXXgf4vad8U9S8bfDHVmngZ76N4wpiJRyBDcRlkKvjnBIxnP63eHvj14F8VfDCbxrpfjPwpqXgy2SSSXX7XV7ebTIljJWRmuVcxAIQQxLcEHNYN9+2Z8H9J8A6f4rvPiv8NrXwtq88ltY6xN4nso9PvZYyQ8cU5l8t2UggqrEjBzQB+RH7Nn/AASc/aK+FX7Dn7MnjiLwTCvxc+AXjbW/EGo+Cb2/t45NXsry7nZlhmV2iEpjfKbmx8wzjFfXPwU+APxa/bJ/4Kn+HP2iPiJ8Nr74O+Ffhh4auNB0LRdV1G2vNV1a6uMGWeT7M7xpCoZlUbiSRnivsK0/bF+Ed9oWkapb/FP4czaZr942n6XeR+JbJoNSuVIDQQuJNskgJAKKSwyOK3/F3xw8FeANei0rXvF3hjRNUms5dQjs7/VYLa4ktohmScI7BjGg5Z8bV7kUAdXRXj+h/wDBQH4D+JdatdN0342fCPUNRvplgtrW28Y6dLNcSMcKiIsxZmJOAAMk10GuftVfDDwx8RIfCGpfEjwHp/i24ZUi0S58QWkWoyswyoW3aQSEkdAF5oA9AopAQwyORS0AFFFFABRRRQAUUUUAFFFFAH5FfCj4Z/Cn4if8Fqv23x8WtJ8H6j4ftNA0ppZdfjgMdrCbLErK8n3PkzlgQRjrXxR8OLvXrn9iH9lRLqXUZvBNv+1TBF4Ge83ljowvofK2l/mKb/M2npjpxX7j/GP/AIJT/s6ftAfE/UfGnjT4ReD/ABF4p1cob7Uru2Zp7rYoVd5DAHCgDkdBXeeO/wBkP4Y/EzQ/B+ma54H8O6jp/gHUINV8OWr2oWHRrqEgxTQquArKQCPpQB+Q/wC094Nf/gkz+1v4++Mnizw/8KP2hvg98ZfGtul093NFL4q8K3TvsWK33Fgyo2/KqMgov3DmvPfEf7K3jf8Abo/b4/bq8B+A/hr8PvEj+LNT0q1fxD4mvhbXHg5XVXE9vGI2eRwqscK6covXpX7Cyf8ABLr9nub4zn4iSfCTwZL41bUG1Q6rLZeZMbps5mwxK7+Sc46816L8Pf2cPAvwo+I/ivxf4b8L6To/ibxzLHPr+o20W2fVXjBCNKc8lQSB9aAPys/Z5+BWj6J/wWzu/hZ+0Bdab4q0r4d/CPR7DwGviMI2n3+2GMXtxCkp2tJ5nm5PJGD6V8eftGafAf2J/wBufwx4OmeX4F2Hxf0e08KpbSF9Pt3e4/0qO1bkbBlOFOAcetfv7+0d+xT8KP2vLWxi+JngHw54zGmMWtG1G2DyW+eoVxhgD6ZxVfUf2GPhBq/wDt/hdcfDvwu3w8tpY7iPQVswlmskb70fauMsG5yec0AfhN+0h4l8bfsyfFz9k/8AZb8ftf6vB4K+Lnh7xD4D8QyqWGqeH7ieHZC795beUtGf9kL6ZOl+0ypf9mf/AIKjBQhY/FHTAA/3SftsPX2r91Pi3+x18L/jv4h8H6t4w8D+H/EOp/D+6jvfDl1eW++XR5o2VkeFuqkMiH6qKxvEP/BPn4K+KvD/AI80rUfht4Yu9O+KF8mpeK4JLYlNduUYMss/PzMGAOeOlAH5Bfs6+Hrj4J/tz+K9O8XaT4Bh8SeN/wBna7udJ/4V1uttHs7WG2cOb63bc5unIB8wvt7BeRX0R+yZ4gsJ/wDg1d1KyS+s3vE+FmtboFmUyr+7uOq5zX3V8Ev+Cb3wJ/Zvi1tfA3wt8JeGv+Eksm07U2tLTD3lsylWhZiSdhBIIBA5rC+H3/BI/wDZr+FM2pyeHPg54N0dtZ0640i9+z27AXNpcLtmhYbsbXHBFAHzp/wb2fDLxT4W/ZW8Cavrej/Aiy0jUvB1l/Zt14V06aDxJcAgH/iYSO5VzjrtUfNXif7Zfw98S/Ej/g4b1Wz8MaT8GdXu4vhbZyzRfEmwlvNOWP7QwJiWN1Il9CTjGa/Rn9nD/gnT8D/2QvFM+t/DP4a+GvBmq3NsbOW406JkZ4cg7OWIxkCoP2gv+Ca3wI/ar+IK+LPiJ8LvC3i3xItqlkNRvoGacQqSVj3Bh8oJP50Afk9+2n+zz498d/8ABcHxn4z+GF9b6d8Tfgr8NdC8UaPY6blNP1dYkVLqwC5/1UsO9UBP90e9ezf8G3f7QNj+1V+1v+2X8RNNtbmxtfFvirTr8WtwhSW2Zopt8bA9CrAj8K/SnwJ+yj8Ofhf8Rn8X6B4P0bSvE0mkQaC2pQRFZ2sIABFbls/cQAYHtTPgh+yV8NP2bfEHijVfAXgrQfCmo+NLsX+uT6db+U2pzgsRJJjgnLN09TQB+VN98NfFXxF/4OGP2lh4Z0f4GasLLS/Dkl4PiNp012sUf2SDm08t12y9eTkdK9y/YL1uw0D/AILy/thrd3lhZK+l+HVjDSrGjYtI+EyelfVvxh/4Jb/s9/H74sXvjrxl8J/CfiHxfqPlfadWuoGNzP5Sqke5gwztVVA+lV/iR/wSl/Z0+MHxIn8YeJvhF4Q1jxPciFZdSngbz5BCipECQwztVFA9gKAPmj/g6D8LW/j7/gnH4e0W4ObXWfiNoFnIQf4JJJUJ/I1+Xvxp8V+LPj5+xZqP7I+vNqCt+yZbeJ9b8SzujBLuzs42i0Zd3/bwMdciFvUV/RV8Xf2dvBHx58Faf4c8ZeGdL8RaFpV5b6haWV5FviguLc5hkUZ+8nasHWP2J/hN4g8R+OdYvfAHhy41T4l6emleKLl7b95rlqiBFhmP8ShQBj2oA/JT4SWmg/EH9uD9hnwt8X1srj4Vf8KRS/8AD1lq7L/Zd9r+ApVlf927iEZAb2rA+Oml6J4H+LH/AAUh8OfCb7HB8H7T4dWlxd2mlNu0m01144/tCw7fkWTO/eq9Dnjiv2F+Jf7DHwh+L/wi0XwH4n+HnhjXPCHhyKODStMu7QPFp6IAEWI/eQAADg9BR4O/Yb+EPw9+BWrfDLQ/h54Y0vwHr0ckWpaLb2gS2vlf74l7vn1JJoA/BH4b6h4o+DfwF1P9hHTm1B4fjXqekeLdHuUVytt4cubFdQ1BQ/bbJBsPOCS471znh/wzdXP/AASd/Yb0jSYPDt1eN8d9YtbSHX4ml0qR/wC0pVVblFIZoScbgCCVzX9DsH7HPwtg8eaH4oXwN4eXxD4a0RvDml6h9mHn2OnMNptUbtHjjFcb4k/4Jcfs+eMPhBovgHU/hN4PvPBnh3UJ9V0zSXtT9nsrqdi80yAHIZ2ZiTnvQB+Wv/BZr9lnVfir4f8A2OPhj4pT4aeFtV8UfEPULKSX4a2slnpVk8kQMU0SOzMJF+RmyeWB7VS/ZV+PPin47/8ABcD4KfC/4xaKR8RvhJ4O13wh4oF1DvttdjUDyLxcja6XEBVz2yx7V+sng/8A4JsfAjwHp/ha00j4YeFrG28E6s+u6FGkDEaXfOArXEWWOHIUDPtXW3/7KHw41P8AaFs/ivceDNCl+I9hZHTrfxCYMX0duQQY9/dcHHNAH5o/s+fs7eEdJ/4LH/tvW+geA/CrXvhXwnot74atU0mDZp14dPV1eBduI3MmDlcEmvn/APZv+H/wO8Yf8G4/xP8AG3jtfD118ZPN1y51bV9TkQeIrfxAt7L9ljDk+cr7hCFVeqnOOSa/b/wt+z34J8EfFzxL490nw3pdh4x8YxQQa1q8UeLnUkhUJEsjZ5CqAB9K858T/wDBMT9n7xj8X/8AhP8AU/hD4HvPF4uFuzqUmnL5kkyjiRlHyM3uVJzz1oAt/wDBNjVPFus/sAfBq78dm5bxjceD9Nk1c3ClZjcG3TeXB53Z617fTIoliQIqhVUYAAwAPSn0AFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQB/9k=';

const togglePhotoSelection = (index: number) => {
  if (selectedPhotos.value.includes(index)) {
    selectedPhotos.value = selectedPhotos.value.filter((i) => i !== index);
  } else if (selectedPhotos.value.length < 2) {
    selectedPhotos.value.push(index);
  }
};

const mergePhotos = () => {
  if (selectedPhotos.value.length === 2) {
    const [firstPhoto, secondPhoto] = selectedPhotos.value.map((index) => capturedPhotos.value[index]);
    const img1 = new Image();
    const img2 = new Image();
    img1.src = firstPhoto;
    img2.src = secondPhoto;
    img1.onload = () => {
      img2.onload = () => {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d') as CanvasRenderingContext2D;
        canvas.width = Math.max(img1.width, img2.width);
        canvas.height = img1.height + img2.height;
        context.drawImage(img1, 0, 0);
        context.drawImage(img2, 0, img1.height);
        const mergedPhotoUrl = canvas.toDataURL('image/jpeg');
        capturedPhotos.value.push(mergedPhotoUrl);
        selectedPhotoToSend.value = mergedPhotoUrl;

        // Deseleccionamos las fotos después de unirlas
        selectedPhotos.value = [];
      };
    };
  }
};

const confirmPhoto = () => {
  if (selectedPhotos.value.length === 1) {
    selectedPhotoToSend.value = capturedPhotos.value[selectedPhotos.value[0]];
  }

  if (selectedPhotoToSend.value && props.record && props.typeImg) {
    console.log ("selectedPhotoToSend.value", selectedPhotoToSend.value);
    const byteString = atob(selectedPhotoToSend.value.split(',')[1]);
    const mimeString = selectedPhotoToSend.value.split(',')[0].split(':')[1].split(';')[0];
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }
    const blob = new Blob([ab], { type: mimeString });
    saveImage(props.record.id, props.typeImg, blob);
    selectedPhotos.value = [];
  }
};

const saveImage = async (index: number, field: string, blob: Blob) => {
  try {
    //console.log("blob", blob);
    const file = new File([blob], 'HC-' + field + '-' + index + '.jpeg', { type: 'image/jpeg' });
    const formData = new FormData();
    formData.append(field, file);

    const response = await $fetch(`api/records/${index}/`, {
      method: 'PATCH',
      body: formData,
      headers: {
        "Content-Type": "multipart/form-data; boundary=----"
      },
    });
    stopStream();
    innerShow.value = false;
  } catch (error) {
    console.error('Error en la solicitud al servidor:', error);
  }
};

const stopStream = () => {
  if (cameraVideoEl.value && cameraVideoEl.value.srcObject) {
    const mediaStream = cameraVideoEl.value.srcObject as MediaStream;
    mediaStream.getTracks().forEach((track) => track.stop());
  }
};

const initStream = async () => {
  stopStream();
  const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: currentCamera.value } });
  if (cameraVideoEl.value) cameraVideoEl.value.srcObject = stream;
};

const toggleCamera = () => {
  currentCamera.value = currentCamera.value === 'user' ? 'environment' : 'user';
  initStream();
};

const takePhoto = () => {
  if (!cameraVideoEl.value) return;
  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d') as CanvasRenderingContext2D;
  canvas.width = cameraVideoEl.value.videoWidth;
  canvas.height = cameraVideoEl.value.videoHeight;
  context.drawImage(cameraVideoEl.value, 0, 0);
  capturedPhotos.value.push(canvas.toDataURL('image/jpeg'));
};

const uploadPhoto = (event: any) => {
  const selectedFile = event.target.files[0];
  const reader = new FileReader();
  reader.onload = (e: ProgressEvent<FileReader>) => {
    if (e.target?.result) capturedPhotos.value.push(e.target.result as string);
  };
  reader.readAsDataURL(selectedFile);
};
const cleanBase64 = (base64String: string): string => {
  // Limpiar posibles saltos de línea, espacios o caracteres no válidos
  return base64String.replace(/[\r\n]/g, '').replace(/\s+/g, '');
};

const addDefaultThumbnail = () => {
  // Limpiar la cadena Base64
  const cleanedBase64 = cleanBase64(defaultThumbnail);

  // Verificar si el prefijo está presente y eliminarlo
  const base64Data = cleanedBase64.split(',')[1]; // Extraer solo la parte Base64

  if (!base64Data) {
    console.error("La cadena Base64 no está correctamente formateada.");
    return;
  }

  try {
    // Aquí directamente usamos la cadena Base64 como fuente de la imagen
    const img = new Image();
    img.src = `data:image/jpeg;base64,${base64Data}`;

    // Cuando la imagen se cargue, la añadimos
    img.onload = () => {
      capturedPhotos.value.push(img.src);
      console.log("Miniatura por defecto añadida:", capturedPhotos.value);
    };
  } catch (error) {
    console.error("Error al procesar la imagen Base64:", error);
  }
};


watch(innerShow, () => {
  if (innerShow.value) initStream();
  else stopStream();
});
</script>

<style scoped>
.camera-modal {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border: 2px solid #007bff;
  border-radius: 10px;
}

.camera-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  width: 100%;
}

.camera-video {
  width: 70%;
}

.buttons-right {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.round-button {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  font-size: 20px;
  background: #007bff;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  border: none;
}

.round-button:hover {
  background: #0056b3;
}

.icon {
  font-size: 24px;
}

.captured-photos {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
}

.photo-item {
  width: 80px;
  height: 80px;
  border: 2px solid transparent;
  cursor: pointer;
}

.photo-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.photo-item.selected {
  border-color: #007bff;
}

.save-merge-buttons {
  display: flex;
  justify-content: space-between;
  width: 100%;
  gap: 10px;
}

.save-btn,
.merge-btn {
  width: 48%;
  padding: 10px;
  font-size: 16px;
  background: #28a745;
  color: white;
  border-radius: 25px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.save-btn:hover,
.merge-btn:hover {
  background: #218838;
}
</style>
