defmodule DiscordBotWeb.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  @impl true
  def start(_type, _args) do
    DiscordBotWeb.Release.migrate()
    children = [
      # Start the Telemetry supervisor
      DiscordBotWeb.Telemetry,
      # Start the Endpoint (http/https)
      DiscordBotWeb.Endpoint
      # Start a worker by calling: DiscordBotWeb.Worker.start_link(arg)
      # {DiscordBotWeb.Worker, arg}
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: DiscordBotWeb.Supervisor]
    Supervisor.start_link(children, opts)
  end

  # Tell Phoenix to update the endpoint configuration
  # whenever the application is updated.
  @impl true
  def config_change(changed, _new, removed) do
    DiscordBotWeb.Endpoint.config_change(changed, removed)
    :ok
  end
end
