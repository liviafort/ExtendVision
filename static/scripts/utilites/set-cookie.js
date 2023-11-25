export function setCookie(nome, valor, diasParaExpirar) {
  var dataExpiracao = new Date();
  dataExpiracao.setTime(dataExpiracao.getTime() + (diasParaExpirar * 24 * 60 * 60 * 1000));
  var expires = "expires=" + dataExpiracao.toUTCString();
  document.cookie = nome + "=" + valor + ";" + expires + ";path=/";
}