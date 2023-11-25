export function setCookie(nome, valor, diasParaExpirar) {
  var dataExpiracao = new Date();
  dataExpiracao.setTime(dataExpiracao.getTime() + (diasParaExpirar * 24 * 60 * 60 * 1000));
  var expires = "expires=" + dataExpiracao.toUTCString();
  document.cookie = nome + "=" + valor + ";" + expires + ";path=/";
}

export function getCookie() {
  let email;
  const cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith("email=")) {
          email = cookie.substring("email=".length);
          break;
      }
  }
  return email;
}