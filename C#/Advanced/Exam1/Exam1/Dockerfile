FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Exam1/Exam1.csproj", "Exam1/"]
RUN dotnet restore "Exam1/Exam1.csproj"
COPY . .
WORKDIR "/src/Exam1"
RUN dotnet build "Exam1.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Exam1.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Exam1.dll"]
