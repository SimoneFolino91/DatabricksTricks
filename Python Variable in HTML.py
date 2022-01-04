import json


personal_data = {
  'name': 'Simone',
  'surname': 'Folino',
  'job':'Data Engineer',
  'signature':'Simon Pholeens'
}

personal_data_js = json.dumps(personal_data) # Create A Json String so you can call the data inside the string for html

# Use the % string formatting so you can use javascript code inside the script tag;
# however this solution prevent the opportunity to use the percentage in css section
# 
displayHTML(
"""
<section>
<h1>Rendering HTML in Databricks</h1>
<h2>Render a Python Variable</h2>
<table style='width: 500px'>
  <td style='width: 250px; text-align: right'>
    <a href='https://www.linkedin.com/in/simone-folino-aa4ab810b/'>
      <img src="https://media-exp1.licdn.com/dms/image/C4D03AQHfntkdBPZfZw/profile-displayphoto-shrink_800_800/0/1631775232573?e=1646870400&v=beta&t=-6NK6gfV5nBzo3Gg_t0aOkaw6HgkyUAbePpAOq9SPvA" style="width: 150px; height: 150px; clip-path: circle()"/>
    </a>
  </td>
  <td>
    <p id='name'></p>
    <p id='surname'></p>
    <p id='job'></p>
  </td>
</table>
<p></p>
<p>Powered by </p>
<p id='signature' style='font-style: italic'></p>
</section>
<script type = 'application/javascript'>
  data_from_python = %s
  
  setTimeout(() => ['name','surname','job'].forEach(x => read(x)), 300)
  setTimeout(() => ['signature'].forEach(x => { document.getElementById(x).innerText = `${data_from_python[x]}`}), 300)
  function read(x){
    document.getElementById(x).innerText = `${capitalize(x)}: ${data_from_python[x]}`
  }
  function capitalize(st){
    let lunghezza = st.length
    return `${st.substring(0,1).toUpperCase()}${st.substring(1,).toLowerCase()}`
  }
</script>
"""%personal_data_js
)
