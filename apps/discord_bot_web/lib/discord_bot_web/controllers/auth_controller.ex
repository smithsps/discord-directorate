defmodule DiscordBotWeb.AuthController do
  use DiscordBotWeb, :controller
  use Ueberauth.Router

  def callback(%{assigns: %{ueberauth_failure: _failure}} = conn, _params) do
    # handle authentication failure
  end

  def callback(%{assigns: %{ueberauth_auth: auth}} = conn, _params) do
    # handle successful authentication
    # `auth` will contain information about the authenticated user
  end
end
