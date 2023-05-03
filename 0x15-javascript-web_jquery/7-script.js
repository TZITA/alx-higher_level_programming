async function fetchName () {
  const response = await fetch('https://swapi-api.alx-tools.com/api/people/6/?format=json');
  const data = await response.text();
  const name = JSON.parse(data).name;
  console.log(name);
  return name;
}

fetchName().then(name => {
  $('DIV#character').text(name);
});
