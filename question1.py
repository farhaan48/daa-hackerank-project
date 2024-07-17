{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMrWUfjA2g/2s+gyECEx339",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/farhaan48/daa-hackerank-project/blob/main/question1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wObDsUYu_t5k",
        "outputId": "87207e7d-9f0e-4771-bca0-c287c559bf25"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "44444\n",
            "ggrgrtg\n",
            "3\n"
          ]
        }
      ],
      "source": [
        "def stringConstruction(s):\n",
        "    # Counting unique characters in the string\n",
        "    unique_chars = set(s)\n",
        "    return len(unique_chars)\n",
        "\n",
        "# Reading input\n",
        "n = int(input().strip())\n",
        "for _ in range(n):\n",
        "    s = input().strip()\n",
        "    result = stringConstruction(s)\n",
        "    print(result)\n"
      ]
    }
  ]
}