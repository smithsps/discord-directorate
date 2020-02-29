let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.pipenv
    pkgs.python37Packages.discordpy
  ];
}
